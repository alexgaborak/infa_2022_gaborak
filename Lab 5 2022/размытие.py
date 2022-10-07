import cv2

# read image
img_src = cv2.imread('sample.jpeg')

# blur the image
img_rst = cv2.blur(img_src, (10, 10))

# save result image
cv2.imwrite('result.jpg', img_rst)
