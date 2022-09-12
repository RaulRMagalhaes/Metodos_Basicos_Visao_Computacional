import cv2 

def limiarizacao(imagem, limiar):
    numLinhas = imagem.shape[0]
    numColunas = imagem.shape[1]

    for l in range(numLinhas):
        for c in range(numColunas):
            if imagem[l][c] > limiar:
                imagem[l][c] = 255
            else: imagem[l][c] = 0
    return imagem

imagem = cv2.imread('../images/pinguins.png', cv2.IMREAD_GRAYSCALE)
limiar = 120

cv2.imshow('Imagem inicial', imagem)

resultado = limiarizacao(imagem,limiar)

cv2.imshow('Limiar = %i'%(limiar), resultado)
cv2.waitKey()