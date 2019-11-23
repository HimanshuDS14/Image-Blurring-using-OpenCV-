import cv2
import numpy as np

image = cv2.imread("lena.jpg")

imag1 = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)


kernel = np.ones([5,5] , dtype=np.float32)/(5*5)

dst = cv2.filter2D(image,-1,kernel=kernel)

blur = cv2.blur(image,(5,5))

gaussian = cv2.GaussianBlur(image,(5,5),0)

cv2.imshow("image" , image)

cv2.imshow("2D convolution" , dst)
cv2.imshow("blur" , blur)
cv2.imshow("gaussian" , gaussian)


cv2.waitKey(0)
cv2.destroyAllWindows()