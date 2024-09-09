import cv2
import os

#get the image
def get_image_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

# saving the image
def save_image(image, subfolder, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, subfolder)
    os.makedirs(path, exist_ok=True)
    cv2.imwrite(os.path.join(path, filename), image)

# loading the image
def load_image(filepath):
    print(f"Loaded image from:  {filepath}")
    image = cv2.imread(filepath)
    if image is None:
        raise FileNotFoundError(f"Image not found at: {filepath}")
    return image

# converting to grayscale
def convert_to_grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # applying gaussian blur
    grayscale_image = cv2.GaussianBlur(grayscale_image, (5,5), 0)
    return grayscale_image

def preview_image(image, window_name="Preview"):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    image_path = get_image_path("receipt.png")
    image = load_image(image_path)
    grayscale_image = convert_to_grayscale(image)
    preview_image(grayscale_image, "Grayscale Preview")
    save_image(grayscale_image, "grayscale", "grayscale_receipt.png")


if __name__ == "__main__":
    main()