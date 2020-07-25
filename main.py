# pip install cmake
# pip install dlib
# pip install opencv-python
# you need to install if pip don't work the Microsoft Visual Build Tools C++  =>> https://visualstudio.microsoft.com/visual-cpp-build-tools/

import cv2
import dlib

detector = dlib.get_frontal_face_detector()

# read the image
img = cv2.imread("your_image.jpg")

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

faces = detector(gray)

for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point

    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(255, 255, 255), thickness=4)


cv2.imshow(winname="Face", mat=img)

cv2.waitKey(delay=0)

cv2.destroyAllWindows()
