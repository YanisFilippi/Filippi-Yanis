import cv2
import matplotlib.pyplot as plt
import numpy as np

print(cv2.__version__)
vidcap = cv2.VideoCapture('TrackBall.mp4')
success,image = vidcap.read()
Video = [image]
print(np.shape(image))
while success:
    success,image = vidcap.read()
    Video.append(image)
frames = len(Video)
print('frames :',frames)
a,b,c = np.shape(Video[0])
Vid = np.zeros((frames,a,b,c))
for i in range(frames):
    Vid[i,:,:,:] = Video[i]

print(Vid[0,:,:,:])
plt.imshow(Vid[0,:,:,:])
plt.show()