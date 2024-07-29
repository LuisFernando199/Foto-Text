# OCR Image to Text

Este proyecto de Python realiza OCR (Reconocimiento Óptico de Caracteres) en una imagen para extraer texto utilizando `pytesseract`. El proyecto incluye dos versiones del script: una utilizando solo `pytesseract` y `PIL`, y otra utilizando `pytesseract` y `OpenCV`.

## Descripción

### Versión 1: Solo con `pytesseract` y `PIL`

Este script carga una imagen, utiliza `pytesseract` para realizar OCR y extrae el texto de la imagen. Luego, muestra la imagen y guarda el texto extraído en un archivo de texto.

### Versión 2: Con `pytesseract` y `OpenCV`

Este script carga una imagen utilizando OpenCV, utiliza `pytesseract` para realizar OCR, muestra la imagen y guarda el texto extraído en un archivo de texto.

## Dependencias

Puedes instalar todas las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Uso

### Versión 1: Solo con `pytesseract` y `PIL`

El siguiente código realiza la extracción utilizando `pytesseract` y `PIL`:

```python
import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Cargamos la imagen
my_image = Image.open('C:\\Users\\0021094\\Desktop\\PYTHON\\ENTORNO_VIRTUAL_FOTO-TEXT\\ocr\\img2.png')

# Extraemos el texto de la imagen
txt = tess.image_to_string(my_image)

# Mostramos la imagen
my_image.show()

# Imprimimos el texto extraído
print(txt)

# Guardamos el texto extraído en un archivo de texto
with open('file1.txt', 'w') as my_file:
    my_file.write(txt + '\n')
```

### Versión 2: Con `pytesseract` y `OpenCV`

El siguiente código realiza la extracción utilizando `pytesseract` y `OpenCV`:

```python
import pytesseract as tess
from PIL import Image
import cv2

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Cargamos la imagen utilizando OpenCV
my_image = cv2.imread('C:\\Users\\0021094\\Desktop\\PYTHON\\ENTORNO_VIRTUAL_FOTO-TEXT\\ocr\\img2.png')

# Extraemos el texto de la imagen
txt = tess.image_to_string(my_image)

# Imprimimos el texto extraído
print(txt)

# Mostramos la imagen y la cerramos al pulsar X
cv2.imshow('Image', my_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardamos el texto extraído en un archivo de texto
with open('file1.txt', 'w') as my_file:
    my_file.write(txt + '\n')
```

## Notas

- Se necesita instalar en windows la app de google: https://github.com/UB-Mannheim/tesseract/wiki
- Asegúrate de modificar la ruta de `tesseract_cmd` según la ubicación de tu instalación de Tesseract.
- Modifica las rutas de las imágenes según la ubicación de tus archivos de imagen.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.


## Archivo de Salida `file1.txt`

El archivo `file1.txt` se sobrescribirá con el texto extraído cada vez que ejecutes el script.
