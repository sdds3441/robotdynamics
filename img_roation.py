import cv2

img=cv2.imread('dataset/triangle.png',cv2.IMREAD_COLOR)
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
print(cX,cY)


M1 = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)
M2 = cv2.getRotationMatrix2D((138, 108), 135, 1.0)
M3 = cv2.getRotationMatrix2D((cX, cY), 180, 1.0)
rotated_90 = cv2.warpAffine(img, M1, (w, h))
rotated_135 = cv2.warpAffine(img, M2, (w, h))
rotated_180 = cv2.warpAffine(img, M3, (w, h))
cv2.imshow('img',img)
cv2.imshow('img_90',rotated_90)
cv2.imshow('img_135',rotated_135)
cv2.imshow('img_180',rotated_180)
cv2.waitKey()
cv2.imwrite('dataset/img_90.png', rotated_90)
cv2.imwrite('dataset/img_135.png', rotated_135)
cv2.imwrite('dataset/img_180.png', rotated_180)