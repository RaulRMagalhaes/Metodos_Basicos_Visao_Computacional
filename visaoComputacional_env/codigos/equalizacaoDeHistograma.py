from copy import deepcopy
import cv2 
import numpy as np
import matplotlib.pyplot as plt

def equalizacao(imagem, min, max):
    resultado = deepcopy(imagem)
    numLinhas = imagem.shape[0]
    numColunas = imagem.shape[1]

    histogramaImagem = histograma(imagem)

    for l in range(numLinhas):
        for c in range(numColunas):
            resultado[l][c] = ((imagem[l][c]-min)/(max-min))*255
    return resultado

def histograma(imagem):
    ocorrenciaCor = np.zeros(256)
    numLinhas = imagem.shape[0]
    numColunas = imagem.shape[1]

    for l in range(numLinhas):
        for c in range(numColunas):
            corImagem = imagem[l][c]
            ocorrenciaCor[corImagem] += 1
    return ocorrenciaCor


imagem = cv2.imread('../images/paisagemBaixoContraste.png', cv2.IMREAD_GRAYSCALE)
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

resultado = deepcopy(imagem)

resultado = equalizacao(resultado, 80, 170)


histogramaInicial = histograma(imagem)
histogramaFinal = histograma(resultado)
histogramaFinal = histogramaFinal*(255/(232*232))


figura = plt.figure(figsize = (8, 8))

plt.subplot(2, 2, 1)
plt.stem(histogramaInicial)
plt.title("a) Histograma inicial", fontsize = 16)

plt.subplot(2, 2, 2)
plt.stem(histogramaFinal)
plt.title("b) Histograma equalizada", fontsize = 16)

plt.subplot(2, 2, 3)
plt.imshow(imagem)
plt.title("c) Imagem inicial", fontsize = 16)

plt.subplot(2, 2, 4)
plt.imshow(resultado)
plt.title("d) Imagem final", fontsize = 16)

plt.suptitle("Equalização", fontsize = 20)
plt.show()