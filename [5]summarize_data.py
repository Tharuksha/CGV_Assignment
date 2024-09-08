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

    print("Applying noise removal and edge detection...")
    edged = cv2.Canny(binary, 30, 200)

    print("Extracting text from image...")
    text = pytesseract.image_to_string(binary)

    return text


# Function to parse and summarize receipt text
def summarize_receipt(text):
    lines = text.split('\n')
    items = []
    cashier = None
    bill_number = None
    subtotal = None
    cash = None
    change = None

    for line in lines:
        line = line.strip()
        if "Cashier" in line:
            cashier = line
        if "Bill" in line:
            bill_number = line
        if "Sub Total" in line or "Subtotal" in line:
            subtotal = line.split()[-1]
        if "Cash" in line and not line.startswith("Cashier"):
            cash = line.split()[-1]
        if "Change" in line:
            change = line.split()[-1]
        if any(char.isdigit() for char in line):
            # Assumption: items have numbers in the line
            items.append(line)






