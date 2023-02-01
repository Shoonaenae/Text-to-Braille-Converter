
import fnmatch
import cv2
import numpy as np
import string
import time
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, LSTM, Reshape, BatchNormalization, Input, Conv2D, MaxPool2D, Lambda, Bidirectional
from keras.models import Model
from keras.activations import relu, sigmoid, softmax
import keras.backend as K
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
import os
import tensorflow as tf
import random
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.utils import shuffle