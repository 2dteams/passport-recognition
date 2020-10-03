from PIL import Image
import pytesseract
import cv2
import numpy as np
import os

image = 'image.jpg'
pytesseract.pytesseract.tesseract_cmd = r'D:\Projects\GIT\passport-recognition\Tesseract-OCR\tesseract.exe'
preprocess = "thresh"

image = cv2.imread(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if preprocess == "thresh":
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((4, 4), np.uint8)
    gray = cv2.erode(thresh, kernel, iterations=1)
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

crop_gray = gray[200:400, 300:1200]
print(pytesseract.image_to_osd(crop_gray))
crop_gray = np.array(Image.fromarray(crop_gray).rotate(-3))
text = pytesseract.image_to_string(crop_gray, lang='rus')
print(text)

filename = "temp.jpg".format(os.getpid())
#
# cv2.imshow('contours', crop_gray)
# cv2.waitKey()
# cv2.destroyAllWindows()

contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

output = image.copy()

for idx, contour in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(contour)
    # print("R", idx, x, y, w, h, cv2.contourArea(contour), hierarchy[0][idx])
    # hierarchy[i][0]: the index of the next contour of the same level
    # hierarchy[i][1]: the index of the previous contour of the same level
    # hierarchy[i][2]: the index of the first child
    # hierarchy[i][3]: the index of the parent
    if hierarchy[0][idx][3] == 0:
        cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 1)


# cv2.imshow("Input", image)
# cv2.imshow("Enlarged", gray)
cv2.imshow("Output", output)
cv2.waitKey(0)
