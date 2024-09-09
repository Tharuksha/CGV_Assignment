import cv2
import numpy as np
import os

def get_image_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)
def save_image(image, subfolder, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, subfolder)
    os.makedirs(path, exist_ok=True)
    cv2.imwrite(os.path.join(path, filename), image)

def correct_perspective(image):
    pts1 = np.float32([[50, 50], [200, 50], [45, 200], [200, 200]])
    pts2 = np.float32([[50, 50], [200, 50], [45, 200], [200, 200]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    corrected_image = cv2.warpPerspective(image, matrix, (320, 630))
    return corrected_image

def preview_image(image, window_name="Preview"):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    binary_path = get_image_path(os.path.join("binarized", "binary_receipt.png"))
    binary_image = cv2.imread(binary_path, cv2.IMREAD_GRAYSCALE)
    corrected_image = correct_perspective(binary_image)
    preview_image(corrected_image, "Perspective Correction Preview")  # Preview the corrected image
    save_image(corrected_image, "corrected", "corrected_receipt.png")

if __name__ == "__main__":
    main()    