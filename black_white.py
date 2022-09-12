import cv2

image = cv2.imread('image.jpg')
# cv2.imshow('',image)
# cv2.waitKey(0)
h,w,d = image.shape
print(type(h))
scale = 0.1
h = int(scale*h)
w = int(scale *w)
imageResized = cv2.resize(image,(h,w))
gray = cv2.cvtColor(imageResized, cv2.COLOR_BGR2GRAY)
for index2,i in enumerate(imageResized):
    for index,j in enumerate(i):

        sum = 0
        for k in j:
            #print(k)
            sum = sum +k
        avg = int(sum/3)
        arr = []
        arr.append(avg)
        i[index] = arr


# cv2.imshow('',imageResized)
# cv2.waitKey(0)
# cv2.imshow('',gray)
# cv2.waitKey(0)
print(gray)