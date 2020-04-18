import cv2
import util

input_image = cv2.imread("prova.jpg")  # B,G,R order

cv2.circle(input_image, (1013,346), 2, util.colors[0], thickness=-1)
cv2.circle(input_image, (913,367), 2, util.colors[0], thickness=-1)


cv2.circle(input_image, (913,301), 2, util.colors[0], thickness=-1)

cv2.imshow("prova",input_image)
cv2.waitKey(0)