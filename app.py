# #Solo con pytesseract
import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

my_image = Image.open('C:\\Users\\0021094\\Desktop\\PYTHON\\ENTORNO_VIRTUAL_FOTO-TEXT\\ocr\\img2.png')
txt = tess.image_to_string(my_image)
my_image.show()
print(txt)
my_file = open('file1.txt', 'w')
my_file.write(txt + '\n')
my_file.close()

#########++++++++++++++++++++############################
#Usando Open cv y guardado en archivo texto

# import pytesseract as tess
# from PIL import Image
# import cv2
# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# my_image = cv2.imread('C:\\Users\\0021094\\Desktop\\PYTHON\\ENTORNO_VIRTUAL_FOTO-TEXT\\ocr\\img2.png')
# txt = tess.image_to_string(my_image)
# print(txt)

# # Abre la imagen y la cierraal pulsar X
# cv2.imshow('Image', my_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Guarda el archivo de texto en la carpeta cuando cerremos la imagen
# my_file = open('file1.txt', 'w')
# my_file.write(txt + '\n')
# my_file.close()

#output = tess.image_path('text_result.txt')