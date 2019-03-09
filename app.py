import numpy as np
import matplotlib.pyplot as plt
import cv2


videoCapture = cv2.VideoCapture(0)

# Initialize plot
figure, axis = plt.subplots()
axis.set_title('RGB Histogram')
axis.set_xlabel('Bin')
axis.set_ylabel('Frequency')

# Initialize plot lines
binCount = 16
lineWidth = 4
lineTransparency = 0.8

redLine, = axis.plot(np.arange(binCount), np.zeros((binCount,)), c='r', lw=lineWidth, alpha=lineTransparency, label='Red')
greenLine, = axis.plot(np.arange(binCount), np.zeros((binCount,)), c='g', lw=lineWidth, alpha=lineTransparency, label='Green')
blueLine, = axis.plot(np.arange(binCount), np.zeros((binCount,)), c='b', lw=lineWidth, alpha=lineTransparency, label='Blue')

axis.set_xlim(0, binCount-1)
axis.set_ylim(0, 1)

axis.legend()

plt.ion()

plt.show()

# Grab, process, and display video frames
while True:
    isFrameRead, frame = videoCapture.read()

    if isFrameRead:
        # Normalize histograms based on number of pixels per frame
        pixelCount = np.prod(frame.shape[:2])

        cv2.imshow('RGB', frame)
        b, g, r = cv2.split(frame)

        redHistogram = cv2.calcHist([r], [0], None, [binCount], [0, 255]) / pixelCount
        greenHistogram = cv2.calcHist([g], [0], None, [binCount], [0, 255]) / pixelCount
        blueHistogram = cv2.calcHist([b], [0], None, [binCount], [0, 255]) / pixelCount

        redLine.set_ydata(redHistogram)
        greenLine.set_ydata(greenHistogram)
        blueLine.set_ydata(blueHistogram)

        figure.canvas.draw()

        # Exit on q key pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

videoCapture.release()
cv2.destroyAllWindows()
