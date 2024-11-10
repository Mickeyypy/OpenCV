import cv2 as cv
img = cv.imread("img/cat.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:#cv.EVENT_LBUTTONUP คือปล่อยเมาส์
         blue = resizedImg[y,x,0]
         green = resizedImg[y,x,1]
         red = resizedImg[y,x,2]

         text = str(blue)+","+str(green)+","+str(red)
         cv.putText(resizedImg,text,(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
         cv.imshow("Output",resizedImg)

#show img
resizedImg = cv.resize(img,(500,500))
cv.imshow("Output",resizedImg)
cv.setMouseCallback("Output",clickPosition)
cv.waitKey(0)
cv.destroyAllWindows()
print(img)
