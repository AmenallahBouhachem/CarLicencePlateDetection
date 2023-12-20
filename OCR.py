import os
# Path to the directory containing the Tesseract executable
import pytesseract 
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'








def extract_text_from_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text
def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)



