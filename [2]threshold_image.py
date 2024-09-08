import cv2
import os

def get_image_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def save_image(image, subfolder, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, subfolder)
    os.makedirs(path, exist_ok=True)
    cv2.imwrite(os.path.join(path, filename), image)

def adaptive_binarize_image(image):
    # Apply adaptive thresholding
    binary_image = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return binary_image