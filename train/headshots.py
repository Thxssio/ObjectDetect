import cv2
import os

name = input("nome:")
os.chdir('dataset')
os.mkdir(name)
os.chdir(name)


cam = cv2.VideoCapture(0)

cv2.namedWindow("Precione espaço para tirar a foto", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Precione espaço para tirar a foto", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Falhou para encontrar o frame")
        break
    cv2.imshow("Precione espaço para tirar a foto", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Fechando...")
        break
    elif k%256 == 32:

        img_name = "image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} Imagem Salva!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
