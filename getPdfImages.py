import fitz
import io
import os
import argparse
from PIL import Image

def extract_images_from_pdf(pdf_file_path, destination_folder):
    pdf_file = fitz.open(pdf_file_path)

    # Create the destination folder if it does not exist
    os.makedirs(destination_folder, exist_ok=True)

    for page_number in range(len(pdf_file)): 
        page = pdf_file[page_number]
        image_list = page.get_images()
        print(image_list)
        
        for image_index, img in enumerate(page.get_images(), start=1):
            print(image_index)
            xref = img[0] 
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            pil_image = Image.open(io.BytesIO(image_bytes))

            image_path = f"{destination_folder}/image_{page_number}_{image_index}.{image_ext}"
            pil_image.save(image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract images from a PDF file.')
    parser.add_argument('pdf_file_path', type=str, help='The path to the PDF file.')
    parser.add_argument('destination_folder', type=str, help='The path to the destination folder.')

    args = parser.parse_args()

    extract_images_from_pdf(args.pdf_file_path, args.destination_folder)