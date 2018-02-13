

import os, sys
import numpy as np
import glob, shutil
import pandas as pd
import tensorflow as tf

test_path = os.listdir('flowers/test')
train_path = os.listdir('flowers/training')
print("Number of test images found: ", len(test_path))
print("Number of train images found: ", len(train_path))


test_dataset = tf.data.Dataset.from_tensor_slices(test_path)
train_dataset = tf.data.Dataset.from_tensor_slices(train_path)

#parse image in the dataset using map function
def _parse_function(test_path):
    image_string = tf.read_file(test_path)
    image_decoded = tf.image.decode_jpeg(image_string, channels=3)
    image = tf.cast(image_decoded, tf.float32)
    return image

test_dataset = test_dataset.map(_parse_function)
test_dataset = test_dataset.batch(2)
train_dataset = train_dataset.map(_parse_function)
train_dataset = train_dataset.batch(2)

#create iterator and input tensor
test_iterator = test_dataset.make_one_shot_iterator()
test_images = test_iterator.get_next()
train_iterator = train_dataset.make_one_shot_iterator()
train_images = train_iterator.get_next()



