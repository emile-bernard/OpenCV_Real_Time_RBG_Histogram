import cv2
import sys
import time
import tkinter as tk
import PIL.Image, PIL.ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from videoCapture import VideoCapture
from canvas import Canvas

class App(tk.Frame):
    UPDATE_DELAY = 150

    BIN_COUNT = 16
    LINE_WIDTH = 4
    LINE_TRANSPARENCY = 0.8

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.videoCapture = VideoCapture(0)
        self.webcamCanvas = Canvas(self.parent, self.videoCapture)

        self.figure, axis = plt.subplots()

        self.histogramCanvas = FigureCanvasTkAgg(self.figure, master=self.parent)
        self.histogramCanvas.get_tk_widget().pack()

        self.initializeRGBPlot(axis)

        self.updateFrame()

    def updateFrame(self):
        isFrameRead, frame = self.videoCapture.getFrame()
        if isFrameRead:
            self.webcamCanvasPhoto = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.webcamCanvas.createImage(0, 0, self.webcamCanvasPhoto, tk.NW)
            self.updateHistogram(frame)
        self.parent.after(self.UPDATE_DELAY, self.updateFrame)

    def updateHistogram(self, frame):
        # Normalize histograms based on number of pixels per frame
        pixelCount = np.prod(frame.shape[:2])
        b, g, r = cv2.split(frame)

        redHistogram = self.getColorHistogram(r, pixelCount)
        greenHistogram = self.getColorHistogram(g, pixelCount)
        blueHistogram = self.getColorHistogram(b, pixelCount)

        self.redLine.set_ydata(redHistogram)
        self.greenLine.set_ydata(greenHistogram)
        self.blueLine.set_ydata(blueHistogram)

        self.histogramCanvas.draw()

    def getColorHistogram(self, color, pixelCount):
        return cv2.calcHist([color], [0], None, [self.BIN_COUNT], [0, 255]) / pixelCount

    def initializeRGBPlot(self, axis):
        # Initialize plot
        axis.set_title('RGB Histogram')
        axis.set_xlabel('Bin')
        axis.set_ylabel('Frequency')

        # Initialize plot lines
        self.redLine, = axis.plot(np.arange(self.BIN_COUNT), np.zeros((self.BIN_COUNT,)), c='r', lw=self.LINE_WIDTH, alpha=self.LINE_TRANSPARENCY, label='Red')
        self.greenLine, = axis.plot(np.arange(self.BIN_COUNT), np.zeros((self.BIN_COUNT,)), c='g', lw=self.LINE_WIDTH, alpha=self.LINE_TRANSPARENCY, label='Green')
        self.blueLine, = axis.plot(np.arange(self.BIN_COUNT), np.zeros((self.BIN_COUNT,)), c='b', lw=self.LINE_WIDTH, alpha=self.LINE_TRANSPARENCY, label='Blue')

        axis.set_xlim(0, self.BIN_COUNT-1)
        axis.set_ylim(0, 1)

        axis.legend()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("OpenCV Webcam RGB Histogram")
    root.resizable(0, 0)
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
