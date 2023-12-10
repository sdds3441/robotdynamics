import cv2

img=cv2.imread('dataset/triangle.png',cv2.IMREAD_COLOR)
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
print(cX,cY)
