# code cant run
import cv2
import datetime

cap = cv2.VideoCapture("img/Newjeans.mp4") #0 คือกล้องตัวเดียว

while (cap.isOpened()):#cap.isOpened() เช็คว่าไม่มีข้อผืดพลาดเกิดขึ้น
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame,currentDate,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),cv2.LINE_4)
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    elif check == False:
        break

cap.release()
cv2.destroyAllWindows()