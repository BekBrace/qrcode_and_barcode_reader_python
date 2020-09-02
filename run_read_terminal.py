import cv2
from pyzbar.pyzbar import decode

img = cv2.imread('q2.png')
decoded_image = decode(img)
# print(decoded_image)
for code in decoded_image:
    print("Type: ", code.type)
    # print("Data:", code.data)
    print("Data: ", code.data.decode('utf-8'))
