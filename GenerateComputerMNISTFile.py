import numpy as np
import cv2
import ConvertToMNIST
from PIL import Image, ImageFilter
import random

def fillImagesLabels(numclasses, imagesperclass, filename):
	images = []
	labels = []
	for i in range(0, numclasses):
		for j in range(0, imagesperclass):		
			image = cv2.imread(filename + "\\"  + str(i) + "\\" + str(j) + ".jpg")
			clustered = ConvertToMNIST.clusterImage(image)
			final = ConvertToMNIST.imageprepare(Image.fromarray(clustered))
			images += [final]
			temp = [0,0,0,0,0,0,0,0,0,0]
			temp[i] = 1
			labels+=[temp]
	return images, labels

def mutualShuffle(images, labels):
	shuffle_indexes = []
	for i in range(0, len(images)):
		shuffle_indexes.append(i)
	random.shuffle(shuffle_indexes)
	images_shuf = []
	labels_shuf = []
	for i in shuffle_indexes:
		images_shuf +=[images[i]]
		labels_shuf +=[labels[i]]
	return np.array(images_shuf), np.array(labels_shuf)


def save(array, name):
	np.save(name + ".npy", array)

images = []
labels = []
images, labels = fillImagesLabels(10, 500, "ComputerMNIST")
images, labels = mutualShuffle(images, labels)
save(images, "ComputerMNISTImages")
save(labels, "ComputerMNISTLabels")