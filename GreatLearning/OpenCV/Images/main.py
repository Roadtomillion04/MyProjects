import cv2

# Make sure to download trained model from opencv github repo
trained_dataset = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

'''Single face'''
# Let's read the image
img01 = cv2.imread(filename ='./img01.jpg')

# can detect both single & multiple faces
face = trained_dataset.detectMultiScale(image = cv2.cvtColor(img01, cv2.COLOR_BGR2GRAY))
# Converting to grayscale coz it's dumb to read rgb lol!
print(face) # returns the face pos coordinates in array


# to unpack a coordinates in list
for (x, y, h, w) in face:                                               # BGR & 255 max amount
    cv2.rectangle(img = img01, pt1 = (x, y), pt2 = (x + w, y + h), color = (255, 0, 0), thickness = 2 )

# to see an image
           # window name
cv2.imshow(winname='face detected', mat=img01) # this closes img in an instant
cv2.waitKey() # waits until you press any key


'''Multi face'''
img02 = cv2.imread(filename ='./img02.jpg')

multi_face = trained_dataset.detectMultiScale(image = cv2.cvtColor(src = img02, code = cv2.COLOR_BGR2GRAY))
print(multi_face)

for (x, y, w, h) in multi_face:
    cv2.rectangle(img = img02, pt1 = (x, y), pt2 = (x + w, y + h), color = (255, 0, 0), thickness = 2)

cv2.imshow(winname='mutiple faces', mat = img02)
cv2.waitKey()

