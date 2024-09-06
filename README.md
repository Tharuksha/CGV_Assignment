# CGV_Assignment

# Receipt Processing and Visualization Project

This project is designed to extract data from shopping receipts using Optical Character Recognition (OCR) and visualize the extracted data. It consists of several Python scripts that handle different parts of the process, from image preprocessing and OCR to data summarization and visualization.

## Project Structure

- `preprocess_image.py`: Converts the receipt image to grayscale.
- `threshold_image.py`: Applies adaptive thresholding to binarize the receipt image.
- `perspective_correction.py`: Corrects the perspective of the receipt.
- `ocr_extraction.py`: Extracts text from the receipt image using Tesseract OCR.
- `summarize_data.py`: Parses the extracted text and summarizes the receipt data.
- `visualize_sales.py`: Visualizes the summarized receipt data using a bar chart.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your machine.
- You have installed the necessary Python libraries (`opencv-python`, `numpy`, `matplotlib`, `pytesseract`).
- Tesseract OCR is installed and properly configured on your system.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Tharuksha/CGV_Assignment.git
    cd CGV_Assignment
    ```

2. **Install required Python packages**:
    Install the required packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Tesseract-OCR**:
    - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract/wiki/Downloads).
    - Add Tesseract to your system's PATH:
      - Windows: Ensure the path to `tesseract.exe` is added to your PATH (typically `C:\Program Files\Tesseract-OCR`).

4. **Verify Tesseract installation**:
    ```bash
    tesseract --version
    ```

## Usage

1. **Preprocess the Image**:
    Convert the receipt image to grayscale:
    ```bash
    python preprocess_image.py
    ```

2. **Binarize the Image**:
    Apply adaptive thresholding to the grayscale image:
    ```bash
    python threshold_image.py
    ```

3. **Correct the Perspective**:
    Correct the perspective of the receipt:
    ```bash
    python perspective_correction.py
    ```

4. **Extract Text from the Image**:
    Extract text from the corrected receipt image using Tesseract OCR:
    ```bash
    python ocr_extraction.py
    ```

5. **Summarize the Receipt Data**:
    Parse and summarize the extracted text:
    ```bash
    python summarize_data.py
    ```

6. **Visualize the Sales Data**:
    Create a bar chart visualization of the summarized data:
    ```bash
    python visualize_sales.py
    ```

## Scripts Overview

### 1. `preprocess_image.py`

- **Functionality**: Loads the receipt image, converts it to grayscale, and applies noise reduction.
- **Command**: 
    ```bash
    python preprocess_image.py
    ```
- **Input**: A receipt image (e.g., `receipt.png`).
- **Output**: A grayscale image saved in the `grayscale` folder.

### 2. `threshold_image.py`

- **Functionality**: Applies adaptive thresholding to the grayscale image to binarize the image (convert it to black and white).
- **Command**:
    ```bash
    python threshold_image.py
    ```
- **Input**: The grayscale image generated in the previous step.
- **Output**: A binarized image saved in the `binarized` folder.

### 3. `perspective_correction.py`

- **Functionality**: Detects the corners of the receipt in the image and applies a perspective correction to get a top-down view of the receipt.
- **Command**:
    ```bash
    python perspective_correction.py
    ```
- **Input**: The binarized image.
- **Output**: A corrected receipt image saved in the `corrected` folder.

### 4. `ocr_extraction.py`

- **Functionality**: Uses Tesseract OCR to extract text from the corrected receipt image.
- **Command**:
    ```bash
    python ocr_extraction.py
    ```
- **Input**: The corrected receipt image.
- **Output**: Extracted text saved in the `extracted_text` folder as `receipt_text.txt`.

### 5. `summarize_data.py`

- **Functionality**: Parses the extracted text to summarize the receipt data (items, subtotal, cash, and change).
- **Command**:
    ```bash
    python summarize_data.py
    ```
- **Input**: The extracted text file (`receipt_text.txt`).
- **Output**: A summarized receipt saved in the `summary` folder as `receipt_summary.txt`.

### 6. `visualize_sales.py`

- **Functionality**: Visualizes the summarized receipt data as a bar chart showing item names and their prices.
- **Command**:
    ```bash
    python visualize_sales.py
    ```
- **Input**: The summarized receipt data (`receipt_summary.txt`).
- **Output**: A bar chart saved in the `visualization` folder as `sales_summary.png`.

## Example Workflow

1. Place your receipt image (`receipt.png`) in the project folder.
2. Run the scripts in the following order:
    1. `preprocess_image.py`
    2. `threshold_image.py`
    3. `perspective_correction.py`
    4. `ocr_extraction.py`
    5. `summarize_data.py`
    6. `visualize_sales.py`
3. The final visualization will be saved as `sales_summary.png` in the `visualization` folder.

## Troubleshooting

- **Tesseract is not recognized**: Ensure Tesseract is installed and added to your system's PATH. Verify the installation using `tesseract --version`.
- **Errors in text extraction**: If Tesseract OCR is producing inaccurate results, consider improving the receipt image quality or using better preprocessing techniques.

## Contributing

If you'd like to contribute to this project, please create a pull request with your changes. Make sure to include detailed descriptions of your updates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
