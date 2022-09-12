from copy import deepcopy
import cv2 
import numpy as np

def filtroDaMedia(imagem):
    numLinhas = imagem.shape[0]
    numColunas = imagem.shape[1]

    matrizHorizontal = [[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]]

    matrizVertical = [[-1, -2, -1],
                      [ 0,  0,  0],
                      [ 1,  2,  1]]

    # cria uma matriz auxiliar copia da imagem porem rodeada de 1
    matrizAux = np.ones((numLinhas+2,numColunas+2))
    for l in range(1,numLinhas+1):
        for c in range(1,numColunas+1):
            matrizAux[l][c] = imagem[l-1][c-1]

    resultadoHorizontal = deepcopy(imagem)
    resultadoVertical = deepcopy(imagem)

    for l in range(numLinhas):
        for c in range(numColunas):
            novoPixel = 0
            subMatriz = matrizAux[l:l+3, c:c+3]
            prod = subMatriz*matrizHorizontal
            for i in prod.flat:
                novoPixel = novoPixel+i
            resultadoHorizontal[l][c] = novoPixel/9
    
    for l in range(numLinhas):
        for c in range(numColunas):
            novoPixel = 0
            subMatriz = matrizAux[c:c+3, l:l+3]
            prod = subMatriz*matrizVertical
            for i in prod.flat:
                novoPixel = novoPixel+i
            resultadoVertical[c][l] = novoPixel/9
    
    for l in range(numLinhas):
        for c in range(numColunas):
            imagem[l][c] = np.sqrt((resultadoHorizontal[l][c]**2) + (resultadoVertical[l][c]**2))
    
    return resultadoHorizontal+resultadoVertical

imagem = cv2.imread('../images/lena-computer-vision.png', cv2.IMREAD_GRAYSCALE)
resultado = deepcopy(imagem)

for i in range(1):
    resultado = filtroDaMedia(resultado)

cv2.imshow('img inicial', imagem)
cv2.imshow('img final', resultado)
cv2.waitKey()
