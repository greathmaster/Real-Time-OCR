# Realtime Optical Character Recognition with Deep Learning  [![Build Status](https://ci.tensorflow.org/buildStatus/icon?job=tensorflow-master-cpu)](https://github.com/michaelzhiluo/OCR-Deep-Learning)
OCR-Deep-Learning uses a webcam projected on a computer screen to identify the digits 0-9. This project uses both MNIST database and my own dataset of computer-digits to train a three-layer Convolutional Neural Network.

The recognition rate for computer digits is around 99.84%, which is a much better improvement than using KNN for recognition (~80%). 

Below are two videos showcasing my project. 

### RestoreModel.py

[![Watch the video](https://j.gifs.com/y8ZgJz.gif)](https://www.youtube.com/watch?v=fZrRL2xBSk0&feature=youtu.be)

### RestoreModelDemo.py

[![Watch the video](https://j.gifs.com/Y6ON7W.gif)](https://www.youtube.com/watch?v=HX0PBi470eY&feature=youtu.be)

## Online Installation 

[Optional (For RestoreModelDemo.py): Download Webcam Images (20k frames, ~4 GB)](https://mega.nz/#F!Yu4n0J5I!Jhk2IacTT-Kcn04DQrFJMQ)

Install [Anaconda](https://repo.continuum.io/archive/Anaconda3-4.4.0-Windows-x86_64.exe) with Enivironmental Variables option selected. 

If installed correctly, the pip command should exist in cmd. 

For the following files to compile, these modules must be installed.
```shell
$ pip install numpy scipy matplotlib opencv-python tensorflow
```

## Installation for Offline Machines

On a computer that can access internet, follow the instructions for "Online Installation".

Next, the .whl files for OpenCV and TensorFlow modules must be downloaded.

On the online computer, create a folder with FOLDER_PATHNAME for .whl files to be stored in.
```shell
$ pip install --download FOLDER_PATHNAME opencv-python tensorflow  
```
Through SSH or real-life means, transfer webcam files, this Repo, and .whl folder to the offline machine.

Keep in mind that both the online and offline machine must be at least a 64 bit machine, as TensorFlow does not have existing .whl files for 32 bit machines.

This installation guides now assumes that:
 * Webcam Images, Git Repo, and .whl file have been downloaded/transferred to offline machine
 * Python and Pip are installed on offline machine. (Transfer Anaconda install file to offline computer if not)
 
On the offline machine, type: 
```shell
$ pip install --no-index --find-links=FOLDER_PATHNAME_IN_OFFLINE_MACHINE opencv-python tensorflow  
```

If this does not work, then your computer may be 32 bit or that the .whl file versions do not fit with Anaconda's requirements.
In that case, create your own custom requirements.txt files and run pip again. If there are still issues, contact me via Github.

## General Overview

### Running Model

* #### TrainMNISTCNN.py
  * This file contains the Tensorflow model and processes the MNIST and my own dataset. The model is saved in OCR-Deep-Learning/MyModel/ folder.

* #### RestoreModel.py
  * This file restores the trained model stored in OCR-Deep-Learning/MyModel and uses OpenCV to process images from webcam and identify the corresponding digits. The user first selects the Region of Interest for each digit. The program will then grab all ROIs and attempt to recognize digits.
 
* #### RestoreModelDemo.py
  * This file draws from 20k webcam images and predetermined ROI to run the Neural Network model.
  
### Dataset Generation

The documentation below shows how I produced the dataset for computer digits. The labelled digits are in OCR-Deep-Learning/ComputerMNIST/. There are 500 digits for each class. The MNIST-dataset representation of these labelled digits are located in ComputerMNISTImages.npy and ComputerMNISTLabels.npy.

* #### GenerateCameraImage.py
  * Using frames from a webcam, this program uses OpenCV library to find the digit's region of interest and crops them out. Examples are shown below:

<img src="http://imgur.com/azAph53.jpg" height="200" width="250"><br>
<img src="http://imgur.com/Fv2SrIW.jpg"> <img src="http://imgur.com/GA0d5sd.jpg"> <img src="http://imgur.com/w8x9Dht.jpg"> <img src="http://imgur.com/3D9idJ6.jpg"> <img src="http://imgur.com/Y3GnWjN.jpg"> <img src="http://imgur.com/sseISo5.jpg"> <img src="http://imgur.com/HOZC3ut.jpg"> <img src="http://imgur.com/qDN25pw.jpg"> <img src="http://imgur.com/yfwGEsd.jpg"> <img src="http://imgur.com/nEl3M1J.jpg"> 

* #### ConvertToMNIST.py
  * General API that helps convert a cropped-digit image from the webcame into the MNIST dataset. Contains three important methods. First method uses K=2-Means clustering to remove noise. The second method resizes and whitens the image to 20x? image and pastes it on a black 28x28 background. The image is further sharpened with the PIL library and converted into a 784x1 numpy array like MNIST images. Last but not least, the final method draws a bounding box around the image in order to get the tightest bounds around the digit.
  
* #### GenerateComputerMNISTFile.py
  * API that uses the labelled digits from OCR-Deep-Learning/ComputerMNIST/ and converts them into a 5000x784 numpy array for images a 5000x10 numpy array for labels. 
  
* #### ComputerMNIST.py
  * A class used in TrainMNISTCNN.py that represents the dataset. Most important method is next_batch which selects a batch of size x from the dataset. 
