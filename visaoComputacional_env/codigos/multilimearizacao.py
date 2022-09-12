from copy import deepcopy
import cv2 

def multilimiarizacao(imagem, limiar1, limiar2):
    numLinhas = imagem.shape[0]
    numColunas = imagem.shape[1]

    for l in range(numLinhas):
        for c in range(numColunas):
            if imagem[l][c] < limiar1:
                imagem[l][c] = 0
            if imagem[l][c] >= limiar1 and imagem[l][c] < limiar2:
                imagem[l][c] = 128
            if imagem[l][c] >= limiar2:
                imagem[l][c] = 255
    return imagem

imagem = cv2.imread('../images/lena-computer-vision.png', cv2.IMREAD_GRAYSCALE)
resultado = deepcopy(imagem)

limiar1 = 90
limiar2 = 150

resultado = multilimiarizacao(resultado, limiar1, limiar2)

cv2.imshow('Imagem inicial', imagem)
cv2.imshow('L1=%i e L2=%i'%(limiar1, limiar2), resultado)
cv2.waitKey()