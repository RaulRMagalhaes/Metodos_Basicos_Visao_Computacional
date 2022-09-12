import cv2 
import numpy as np 
import matplotlib.pyplot as plt

R = 0
G = 1
B = 2

img = img3 = cv2.imread('lena-computer-vision2.png', cv2.IMREAD_COLOR)

numLinhas = img.shape[0]
numColunas = img.shape[1]

#for l in range(numLinhas):
#    for c in range(numColunas):
#        img[l][c][R] = 0
#        img[l][c][G] = 0
#        img[l][c][B] = 255


cv2.imshow('Imagem inicial', img)

for l in range(numLinhas):
    n = 200
    for c in range(numColunas):
        if img3[l][c][R] > n:
            img3[l][c][R] = 255
        else: img3[l][c][R] = 0

        if img3[l][c][G] > n:
            img3[l][c][G] = 255
        else: img3[l][c][G] = 0

        if img3[l][c][B] > n:
            img3[l][c][B] = 255
        else: img3[l][c][B] = 0

cv2.imshow('Imagem final', img3)
cv2.waitKey(0)

cv2.destroyAllWindows()