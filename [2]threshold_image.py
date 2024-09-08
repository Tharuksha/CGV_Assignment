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

def preview_image(image, window_name="Preview"):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    grayscale_path = get_image_path(os.path.join("grayscale", "grayscale_receipt.png"))
    grayscale_image = cv2.imread(grayscale_path, cv2.IMREAD_GRAYSCALE)
    binary_image = adaptive_binarize_image(grayscale_image)
    preview_image(binary_image, "Adaptive Thresholding Preview")
    save_image(binary_image, "binarized", "binary_receipt.png")

if __name__ == "__main__":
    main()