import cv2
import pytesseract
from pytesseract import Output
from PTL import Image
import numpy as np

# Function to process the receipt image and extract text
def process_image(image_path):
    
    print("Loading image...")
    img = cv2.imread(image_path)

    print("Converting to grayscale...")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print("Applying binarization...")
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    





