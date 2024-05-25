import cv2
import argparse
from pdf2image import convert_from_path

# Create an argument parser
parser = argparse.ArgumentParser(description='Convert PDF pages to images and apply template matching.')
parser.add_argument('pdf_file_path', type=str, help='The path to the PDF file.')
parser.add_argument('template_path', type=str, help='The path to the template image.')

# Parse the arguments
args = parser.parse_args()

# Convert PDF to list of images
images = convert_from_path(args.pdf_file_path)

# Load the template
template = cv2.imread(args.template_path, 0)
w, h = template.shape[::-1]

# Iterate over the images
for image in images:
    # Convert PIL Image to cv2 Image
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Apply template matching
    res = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)