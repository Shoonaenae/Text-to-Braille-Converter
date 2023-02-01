#Importing required libraries.
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from keras.layers import *
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
import random
import math

image_list=os.listdir('/content/Dataset1/img/')
image_list=[filename.split(".")[0]for filename in image_list]