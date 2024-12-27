# README

## Expose API Using Ngrok for OCR Recognition

This project demonstrates how to expose an OCR (Optical Character Recognition) API using Ngrok and integrate it with a Python script. The exposed API takes an image URL as input and returns the OCR recognition result.

### Prerequisites

1. **Python Environment**: Make sure Python 3.12 or higher is installed.
2. **Ngrok Setup**: Install and configure Ngrok for exposing local services to the internet.
3. **Required Python Libraries**: Install `requests` library using the following command:
   ```bash
   pip install requests
   ```
4. **Internet Access**: Ensure the system has access to the internet for making API requests.

### Project Structure

- `perform_ocr(img_path)`: A Python function that sends a POST request to the OCR API endpoint with the image URL.
- Sample test image URL:
  ```
  https://keko.vn/uploads/product/GIAY_IN_HOA_DON/giay_in_hoa_don_k80/SAN_PHAM_GIAY_IN_BILL_K80X45.jpg
  ```

### Usage

1. **Start the Ngrok Service**:
   Ensure your OCR API is running locally, then expose it using Ngrok. For example:
   ```bash
   ngrok http 5000
   ```
   Replace the `https://b9d1-34-19-7-241.ngrok-free.app/ocr` URL in the code with your Ngrok forwarding URL.

2. **Run the Python Script**:
   Use python file `main.py` in your Python environment:

3. **Test the API**:
   - Replace `img_path` with the URL of the image you want to process.
   - The script will send the image URL to the exposed Ngrok endpoint and print the OCR recognition result.

### Expected Output

When running the script with a valid image URL, the OCR result will be printed to the console. For example:
```text
Response in = 0.234
OCR Recognition Result:
"
| MẶT HÀNG | SL | ĐVT | Giá | T Tiền |
|---|---|---|---|---|
| áo dạ cài pk | 1 | cái | 1,499,000 | 1,499,000 |
| áo dạ khuy cổ lông | 1 | cái | 1,690,000 | 1,690,000 |
| áo dạ sát nách | 1 | cái | 1,210,000 | 1,210,000 |
| áo dạ sát nách | 1 | cái | 870,000 | 870,000 |
| áo dạ sát nách | 1 | cái | 1,210,000 | 1,210,000 |
"
```

If the API encounters an error, the error message and status code will be displayed.

### Notes

- Ensure the Ngrok endpoint URL is correct and active before running the script.
- The `image_url` parameter in the JSON payload must be publicly accessible.

### Troubleshooting

1. **Ngrok URL Expired**:
   If the Ngrok URL changes, update the `perform_ocr` function with the new URL.

2. **HTTP Errors**:
   Check the API status and ensure the local server is running properly.

3. **Invalid Image URL**:
   Ensure the provided image URL is valid and accessible.

### License

This project is open-source and can be freely used and modified.