import cv2 as cv

img = cv.imread("img/cat.jpg")
resizeimg = cv.resize(img,(700,700))
#วาดเส้นตรง
# line(ภาพ, จุดเริ่มต้น(x,y),จุดสุดท้าย(x,y), สี(BGR),ความหนา)

cv.arrowedLine(resizeimg,(100,100),(500,200),(255,0,00),10)
cv.putText(resizeimg,"cat",(200,200),3,2.5,(0,0,255)) #ดูใน document ของ openCV
cv.imshow("output",resizeimg)
cv.waitKey(0)
cv.destroyAllWindows()