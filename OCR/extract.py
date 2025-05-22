import pytesseract
import cv2
import os
import sys

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set the image folder path relative to where the script is
input_folder = os.path.join(os.path.dirname(__file__), "images")
output_file = "output.txt"

# Check if folder exists
if not os.path.exists(input_folder):
    print(f"❌ Folder '{input_folder}' not found! Please create it and add images.")
    sys.exit()

# OCR processing
with open(output_file, "w") as f:
    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)
            text = pytesseract.image_to_string(img)
            f.write(f"--- {filename} ---\n{text}\n\n")
            print(f"OCR for {filename}:\n{text}\n")




