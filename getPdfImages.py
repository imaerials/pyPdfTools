import fitz
import io
from PIL import Image

pdf_file = fitz.open("catalogo_saphirus.pdf")

for page_number in range(len(pdf_file)): 
    page=pdf_file[page_number]
    image_list = page.get_images()
    print(image_list)
    
    for image_index, img in enumerate(page.get_images(),start=1):
        print(image_index)
        xref = img[0] 
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        pil_image = Image.open(io.BytesIO(image_bytes))

        image_path = f"image_{page_number}_{image_index}.{image_ext}"
        pil_image.save(image_path)