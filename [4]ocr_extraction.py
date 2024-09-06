import cv2
import pytesseract
import os

def get_image_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def save_text(text, subfolder, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, subfolder)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, filename), "w") as text_file:
        text_file.write(text)

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

def main():
    corrected_path = get_image_path(os.path.join("corrected", "corrected_receipt.png"))
    corrected_image = cv2.imread(corrected_path, cv2.IMREAD_GRAYSCALE)
    extracted_text = extract_text(corrected_image)
    save_text(extracted_text, "extracted_text", "receipt_text.txt")

if __name__ == "__main__":
    main()
