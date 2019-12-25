import numpy as np
from numpy import matlib
#a = np.array([[1,2,3],[4,5,6]])
#print(type(a))
#print(a.shape)
'''
#1

a = np.random.randint(0,10,size=[4,3,2])
dictNP = {'ndim':a.ndim,'shape':a.shape,'size':a.size,'dtype':a.dtype,'itemsize':a.itemsize,'data':a.itemsize }
print(dictNP)

#2

#a1 = np.random.randint(0,8, size=[3,3])
#a2 = np.random.randint(2,10,size=[3,3])
b1= np.matlib.random.randint(0,8,size=[3,3])
print('b1:')
print(b1)
b2=np.matlib.random.randint(2,10,size=[3,3])
print('b2:')
print(b2)
produitDot=np.dot(b1,b2)
print('produit de dot:')
print(produitDot) #print(np.matmul(b1,b2))
print('produit de * : ')
print(b1*b2)
print('Transposer b1')
print(b1.T)
'''
#3
c = np.matlib.random.randint(0,10,size=[3,3])
print('le matrice c:')
print(c)
print('le déterminant de c:')
print(round(np.linalg.det(c),3))
print('l’inverse de c:')
cinv=np.linalg.inv(c)
print(cinv)
print('D:')
d=np.array([[2],[3],[4]])
print(d)
print("Résoudre un système d’équations linéaires 'CX=D' :")
print(np.linalg.solve(cinv,d))
print('valeurs propres de c:')
eigenvalue,featurevector=np.linalg.eig(c)
print(eigenvalue)
print('vecteurs propres de c:')
print(featurevector)