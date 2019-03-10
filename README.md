# OpenCV_Real_Time_RBG_Histogram
This project contains a basic python script to run opencv-python with a webcam stream and plot the RBG histogram.

## Previews


## How it work's
Histograms are collected counts of data organized into a set of predefined bins.

Let's take this matrix containing information (intensity in the range 0 to 255) on an image:

![Matrix](./documentation/Matrix.jpg?raw=true"Matrix")

Since we know that the range of information value for this case is 256 values, we can segment our range in subparts (called bins) and we can keep count of the number of pixels that fall in the range of each bin.

Applying this to the example above we get the image below ( axis x represents the bins and axis y the number of pixels in each of them):

![Bin](./documentation/Bin.jpg?raw=true"Bin")

Histograms contains:

- bins: It is the number of subdivisions in each dim. In our example, bins = 16

- range: The limits for the values to be measured. In this case: range = [0, 255]

## How to setup
- Install opencv-python
```
$ pip install opencv-python
```

- Install tkinter
```
$ pip install tkinter
```

- Install pillow
```
$ pip install pillow
```

- Install matplotlib
```
$ pip install matplotlib
```

- Install numpy
```
$ pip install numpy
```

## Links
- [Python Patterns - Github](https://github.com/faif/python-patterns)
- [Python Design Patterns: For Sleek And Fashionable Code](https://www.toptal.com/python/python-design-patterns)
- [Histogram Calculation](https://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/histogram_calculation/histogram_calculation.html)
