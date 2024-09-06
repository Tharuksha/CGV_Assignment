import cv2
import pytesseract

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    corrected_image = cv2.imread("corrected_receipt.png", cv2.IMREAD_GRAYSCALE)
    extracted_text = extract_text(corrected_image)
    with open("receipt_text.txt", "w") as text_file:
        text_file.write(extracted_text)
