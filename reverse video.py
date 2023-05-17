#Reversing a Video
import cv2

cap = cv2.VideoCapture('video.mp4')
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
for i in reversed(range(num_frames)):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    cv2.imshow('Reverse Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
