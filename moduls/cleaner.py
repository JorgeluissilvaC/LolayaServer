import unicodedata
import string
import re

#Hunspell corrector ortografico

def strip_accents(s):
	return text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

def fix_accent(text):
	return text.replace('à','á').replace('è','é').replace('ì','í').replace('ò','ó').replace('ù','ú')

def clean(text):
	texto = fix_accent(' '.join(str(text).split())).replace('°', ".")
	return re.sub('[^a-zA-Z0-9_\-.,ñÑ()"áÁéÉíÍóÓúÚ/ ]', '', texto)



"""
https://machinelearningmastery.com/clean-text-machine-learning-python/

Eliminar los indices 1. ..
sobre espacios
eliminar tildes
remover textos repetidos
y/o
3,6-Dihidroxy-2-(11-phenylundecanoyl)cyclohex-2-en-1-one
linea 216
"""