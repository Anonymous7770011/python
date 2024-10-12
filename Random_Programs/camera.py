import cv2
from os import system as sys

cap = cv2.VideoCapture(0)  # 0 for default camera

# Set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 10)
data='''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''
while True:
    ret, frame = cap.read()

    if not ret:
        break

    image=cv2.imread('frame',frame)
    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('grayimg',grayimg)
    shape=grayimg.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            v=int(((grayimg[i][j])/69)
            print(data[v]+"",end="")
        print()
    sys("cls")

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()