import cv2

trained_model = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

# to load a video
video = cv2.VideoCapture('2020-10-17 11-16-46.mkv')
color = (255, 0, 0)

# videos are frames of images, to read a video
# success, frame = video.read()
# cv2.imshow(winname='video', mat=frame)
# cv2.waitKey()
# Thus it gives the first frame of image. We need a loop to play the all frames in video

while True:
    ret, frame = video.read()
    if ret: # remains true until no frame found
        capture_face = trained_model.detectMultiScale(image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        for (x, y, w, h) in capture_face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.imshow(winname='video', mat=frame)
        key = cv2.waitKey(delay = 1)
        if key == ord('Q') or key == ord('q'): # ord gives ascii/unicode that key requires 
            break
    else:
        print('Video Completed')
        break

