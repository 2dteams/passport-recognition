from PIL import Image
import pytesseract
import cv2
import numpy as np
import os

image = 'image.jpg'
pytesseract.pytesseract.tesseract_cmd = r'D:\Projects\GIT\passport-recognition\Tesseract-OCR\tesseract.exe'
preprocess = "thresh"

# загрузить образ и преобразовать его в оттенки серого
image = cv2.imread(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# проверьте, следует ли применять пороговое значение для предварительной обработки изображения
if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# если нужно медианное размытие, чтобы удалить шум
elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

# сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR
filename = "temp.jpg".format(os.getpid())
# filename = '222.jpg'
cv2.imwrite(filename, gray)

# загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
pytesseract.pytesseract.tesseract_cmd = os.getcwd() + r'\Tesseract-OCR\tesseract.exe'
temp_image = Image.open(filename)
text = pytesseract.image_to_string(temp_image, lang='rus')
degrot = pytesseract.image_to_osd(temp_image)
tt = degrot.rfind('Orientation confidence: ') + len('Orientation confidence: ')
temp_image = temp_image.rotate(-float(degrot[tt: tt + 4]))
tt = np.array(temp_image.convert('RGB'))[:, :, ::-1]
cv2.imwrite(filename, cv2.cvtColor(tt, cv2.COLOR_BGR2GRAY))
# print(float(degrot[tt: tt + 4]))
# os.remove(filename)

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
