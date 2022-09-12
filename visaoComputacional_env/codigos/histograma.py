import cv2 
import numpy as np
import matplotlib.pyplot as plt

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

histograma = histograma(imagem)

figura = plt.figure(figsize = (8, 3))

plt.subplot(1, 2, 1)
plt.imshow(imagem)
plt.title("a) Imagem", fontsize = 16)

plt.subplot(1, 2, 2)
plt.stem(histograma)
plt.title("b) Histograma da imagem", fontsize = 16)

plt.show