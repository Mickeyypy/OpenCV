import cv2 as cv
img = cv.imread("img/cat.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:#cv.EVENT_LBUTTONUP คือปล่อยเมาส์
         text = str(x)+","+str(y)
         cv.putText(img,text,(x,y),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv.LINE_4)
         cv.imshow("Output",img)
#ทำงานกับ mouse


#show img
cv.imshow("Output",img)
cv.setMouseCallback("Output",clickPosition)
cv.waitKey(0)
cv.destroyAllWindows()

