import cv2
file=open(r"C:\Users\akfla\Documents\Programs\python\Random_Programs\data\statue.txt","w")
data='''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''
image=cv2.imread(r"C:\Users\akfla\Documents\Programs\python\Random_Programs\data\statue.png")
#cv2.imshow('image',image)
grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('grayimg',grayimg)
cv2.waitKey(0)
shape=grayimg.shape
for i in range(shape[0]):
    for j in range(shape[1]):
        v=int(((grayimg[i][j])//70))
        #v=int(((grayimg[i][j])/255)*69)
        file.write(data[-v]+"")
    file.write("\n")
