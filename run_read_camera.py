import cv2
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    _, frame = cap.read()
    decodedObjects = decode(frame)
    for obj in decodedObjects:
        # print("Data: ", obj.data)
        cv2.putText(frame, str(obj.data), (20, 20),
                    font, 1, (255, 122, 54), 3)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
