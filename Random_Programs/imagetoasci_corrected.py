import cv2
file=open(r"C:\Users\akfla\Documents\Programs\python\Python\data.txt","w")
data='''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
image=cv2.imread(r"C:\Users\akfla\Documents\Programs\python\Python\images\image.png")
#cv2.imshow('image',image)
grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('grayimg',grayimg)
cv2.waitKey(0)
w=80
h=170
shape=grayimg.shape
for i in range(0,shape[0],shape[0]//w):
    for j in range(0,shape[1],shape[1]//h):
        v=int(((grayimg[i][j])/255)*(len(data)-1))
        file.write(data[v]+"")
    file.write("\n")
