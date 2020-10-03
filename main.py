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
    gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((4, 4), np.uint8)
    gray = cv2.erode(gray, kernel, iterations=1)
    gray = cv2.dilate(gray, np.ones((5, 5), np.uint8), iterations=1)

filename = "temp.jpg".format(os.getpid())
# filename = '222.jpg'
cv2.imwrite(filename, gray)

pytesseract.pytesseract.tesseract_cmd = os.getcwd() + r'\Tesseract-OCR\tesseract.exe'
temp_image = Image.open(filename)
degrot = pytesseract.image_to_osd(temp_image)
tt = degrot.rfind('Orientation confidence: ') + len('Orientation confidence: ')
temp_image = temp_image.rotate(-float(degrot[tt: tt + 4]))
tt = np.array(temp_image.convert('RGB'))[:, :, ::-1]
tt = cv2.rectangle(cv2.cvtColor(tt, cv2.COLOR_BGR2GRAY), (350, 200), (1200, 400), (255, 0, 0), 2)
cv2.imwrite(filename, tt)
# print(float(degrot[tt: tt + 4]))
temp_image = Image.open(filename)
text = pytesseract.image_to_string(temp_image, lang='rus')
# os.remove(filename)
print(text)

# показать выходные изображения
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
# input(‘pause…’)

#
# cap = cv2.VideoCapture(0)
#
# while True:
#     # orig_img = ImageGrab.grab(box)
#     ret, orig_img = cap.read()
#
#     np_im = np.array(orig_img)
#
#     img = cv2.cvtColor(np_im, cv2.COLOR_BGR2GRAY)
#
#     text = pytesseract.image_to_string(img)
#
#     cv2.imshow('window', img)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#
#     print(text)
