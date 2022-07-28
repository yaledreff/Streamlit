
import cv2
import numpy as np
import skimage.morphology as mph
from skimage.measure import label, regionprops
import io

color_map = {
 '0': [0, 0, 0],
 '1': [153, 153, 0],
 '2': [255, 204, 204],
 '3': [255, 0, 127],
 '4': [0, 255, 0],
 '5': [0, 204, 204],
 '6': [255, 0, 0],
 '7': [0, 0, 255]
}


def get_bytes_value(image):
 img_byte_arr = io.BytesIO()
 image.save(img_byte_arr, format='JPEG')
 return img_byte_arr.getvalue()