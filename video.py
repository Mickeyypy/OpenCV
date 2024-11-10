# code cant run
import cv2

cap = cv2.VideoCapture("img/Newjeans.mp4") #0 คือกล้องตัวเดียว

while (cap.isOpened()):#cap.isOpened() เช็คว่าไม่มีข้อผืดพลาดเกิดขึ้น
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:
        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Output",grey)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    elif check == False:
        break

cap.release()
cv2.destroyAllWindows()