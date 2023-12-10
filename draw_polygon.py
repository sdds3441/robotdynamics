import cv2
import numpy as np

img = np.zeros(shape=(256, 256, 3), dtype=np.uint8)
space = (256 - 100 * np.sqrt(3)) / 2
triangle = np.array([[28, space], [228, space], [128, 256 - space]], dtype=np.int32)

cv2.fillConvexPoly(img, triangle, color=(0, 0, 255))

cv2.line(img, (128, round(256 - space)), (128, round(256 - space)), (255, 0, 0), 10)
cv2.imshow('img', img)
cv2.waitKey()
cv2.imwrite('dataset/triangle.png', img)