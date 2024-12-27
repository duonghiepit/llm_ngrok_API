import requests

def perform_ocr(img_path):
    response = requests.post(
        "https://b9d1-34-19-7-241.ngrok-free.app/ocr",
        json={
            "image_url": img_path,
        }
    )
    print("Response in = ", response.elapsed.total_seconds())
    if response.status_code == 200:
        return response.json().get("response_message")
    else:
        print("Error:", response.status_code, response.text)
        return None
    
img_path = "https://keko.vn/uploads/product/GIAY_IN_HOA_DON/giay_in_hoa_don_k80/SAN_PHAM_GIAY_IN_BILL_K80X45.jpg"

result = perform_ocr(img_path)
if result:
    print("OCR Recognition Result: ")
    print(result)
else:
    print("Cannot!")