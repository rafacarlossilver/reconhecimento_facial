#!/usr/bin/env python
# -*- coding: windows-1252 -*-
from PIL import Image # Importando o m�dulo Pillow para abrir a imagem no script

import pytesseract # M�dulo para a utiliza��o da tecnologia OCR

print( pytesseract.image_to_string( Image.open('/var/www/python/reconhecimento_facial/fotos/textos-para-imprimir-leituras-para-imprimir .jpg') ) ) # Extraindo o texto da imagem