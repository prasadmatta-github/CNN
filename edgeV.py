import cv2
import numpy as np

img = cv2.imread('/home/prasadmatta/CNN/black.jpg')
# img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()