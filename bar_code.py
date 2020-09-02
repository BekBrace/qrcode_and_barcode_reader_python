import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(3, 480)  # height

camera = True

while camera:
    success, frame = cap.read()
    for code in decode(frame):
        print(code.type)
        print(code.data.decode('utf-8'))
    cv2.imshow('barcode scanning...', frame)
    cv2.waitKey(1)
