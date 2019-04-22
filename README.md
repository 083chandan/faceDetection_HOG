# Face detection using HOG (Histogram of Oriented Gradients)
Face detection using HOG

Compiled version of dlib-19.17.0 for python 3.6 is placed in libraries in case any issues while installing the libraries.

For testing very few dataset of the known personalites is collected and trained. Dataset folder names will be used to label the output.
Untrained faces will be labelled as "unknown".


### REQUIREMENTS

python 3.6

openCV 4

> additional libraries are in requirements.txt
> Install dlib first and the run requirements.txt


***(if you want to run .ipynb files in docs folder install jupyter notebook)***

### EXECUTE

``` bash
python faceRecognition.py
```

**Explanation on HOG and features extraction is in the docs folder**
https://github.com/083chandan/faceDetection_HOG/blob/master/docs/hog.pdf

#### Training with additional dataset

1. Place the dataset to train in dataset folder (dataset should be segregated and named accordingly)

2. Run **trainFaces.py** to train with new dataset

3. Once the training is complete, new dataset model will be saved in the root folder with the filename **faceModel.pickle**


### OUTPUT

![OUTPUT](https://github.com/083chandan/faceDetection_HOG/blob/master/output/Capture.PNG)


### REFS
https://www.learnopencv.com/histogram-of-oriented-gradients/
