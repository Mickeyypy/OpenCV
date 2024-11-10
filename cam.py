# code cant run
import cv2

cap = cv2.VideoCapture(0) #0 คือกล้องตัวเดียว

while (True):
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    cv2.imshow("Output",frame)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()