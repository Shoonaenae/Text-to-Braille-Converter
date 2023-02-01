import random
from vis_pad_batch_defn_ocr import image_list

random.shuffle(image_list)
file_train=image_list[0:int(0.75*len(image_list))]
file_test=image_list[int(0.75*len(image_list)):]