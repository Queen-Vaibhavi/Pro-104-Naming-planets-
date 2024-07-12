import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(100,380),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,255,0))
cv2.putText(img,"Mercury",(76,80),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,255,0))
cv2.putText(img,"Venus",(170,150),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,255,0))
cv2.putText(img,"Earth",(260,290),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,255,0))
cv2.putText(img,"Mars",(360,150),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,255,0))
cv2.putText(img,"Jupiter",(510,70),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,255,0))
cv2.putText(img,"Saturn",(720,110),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,255,0))
cv2.putText(img,"Uranus",(930,130),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,255,0))
cv2.putText(img,"Neptunes",(1080,300),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 1,color = (0,255,0))

cv2.imshow("solar system" ,img)
cv2.waitKey(0)
cv2.imwrite("solar-system.jpg",img)