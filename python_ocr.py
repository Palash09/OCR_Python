import io
import json
import cv2
import numpy as np 
import requests

img = cv2.imread("book_image.jpeg")
height, width, _ = img.shape

#For removing unwanted part of image
roi = img[220: height, 72: width]

#For performing OCR operations on our Image
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpeg",roi,[1,90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
				files = {"book_image.jpeg":file_bytes},
				data = {"apikey":"a000e7050888957",
						"language":"eng"})

result = result.content.decode()
result = json.loads(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")

print(text_detected)

cv2.imshow("roi", roi)
cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()