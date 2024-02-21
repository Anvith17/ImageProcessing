import cv2 as cv

img = cv.imread('C:\Task01\Resources\photos\cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('C:\Task01\Resources\videos\dog.mp4')

while True:
    isTrue, frame = capture.read()

    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()