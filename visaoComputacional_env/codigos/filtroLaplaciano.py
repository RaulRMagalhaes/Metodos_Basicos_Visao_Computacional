import cv2 
import numpy as np
from copy import deepcopy

def filtroLaplaciano(imagem):
    numLinhas = imagem.shape[0]
    numColunas = imagem.shape[1]

    matrizPassaAlta = [[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]]

    # cria uma matriz auxiliar copia da imagem porem rodeada de 1
    matrizAux = np.ones((numLinhas+2,numColunas+2))
    for l in range(1,numLinhas+1):
        for c in range(1,numColunas+1):
            matrizAux[l][c] = imagem[l-1][c-1]

    for l in range(numLinhas):
        for c in range(numColunas):
            novoPixel = 0
            subMatriz = matrizAux[l:l+3, c:c+3]
            prod = subMatriz*matrizPassaAlta
            for i in prod.flat:
                novoPixel = novoPixel+i
            imagem[l][c] = novoPixel
    
    return imagem
        
imagem = cv2.imread('../images/foto.jpg', cv2.IMREAD_GRAYSCALE)
resultado = deepcopy(imagem)

for i in range(3):
    resultado = filtroLaplaciano(resultado)

cv2.imshow('img inicial', imagem)
cv2.imshow('img final', resultado)
cv2.waitKey()
