import cv2
img = cv2.imread("butterfly.jpg")
cv2.imshow("display image",img)
greyimg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("greyscale",greyimg)
print(greyimg)
cv2.waitKey(0)