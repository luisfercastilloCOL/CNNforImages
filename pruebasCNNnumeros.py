import cv2

from prediccion import prediccion

#categorias=["Huevos","Arepas",...]
categorias=["0","1","2","3","4","5","6","7","8","9"]
reconocimiento=prediccion()
imagenPrueba=cv2.imread("test/5/5_11.jpg",0)
indiceCategoria=reconocimiento.predecir(imagenPrueba)
print("La imamgen cargada es ",categorias[indiceCategoria])
while True:
    cv2.imshow("imagen",imagenPrueba)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cv2.destroyAllWindows()