import imageio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img=imageio.imread('chien.jpg')
#l’image originale
plt.imshow(img)
plt.show()
print(np.shape(img))
print(img.size)
#réduite en taille
img1 = np.array(Image.fromarray(img).resize((100,100)))
imageio.imwrite('chien2.jpg',img1)
plt.imshow(img1)
plt.show()
print(np.shape(img1))