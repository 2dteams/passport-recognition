from PIL import Image
import pytesseract
import cv2
import os

image = 'test.jpg'

preprocess = "thresh"

# загрузить образ и преобразовать его в оттенки серого
image = cv2.imread(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# проверьте, следует ли применять пороговое значение для предварительной обработки изображения

if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# если нужно медианное размытие, чтобы удалить шум
elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

# сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR

filename = "222.jpg".format(os.getpid())
# filename = '222.jpg'
cv2.imwrite(filename, gray)

# загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
text = pytesseract.image_to_string(Image.open(filename), lang='rus')
# os.remove(filename)
print(text)

# показать выходные изображения
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
# input(‘pause…’)


# import numpy as np
# import cv2
# from PIL import ImageGrab
# import pytesseract
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
