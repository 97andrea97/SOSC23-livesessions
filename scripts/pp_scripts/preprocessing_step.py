################################### EXERCISE INSTRUCTIONS
#Define the following logics in this file:

#Create an infinite while loop;
#Make sure looping does not consume all your CPU spinning on no-ops by introducing a pause of few tens of milliseconds using time.sleep.
#Use glob.glob to loop over the PNG files in the /input folder;
#For each absolute file name detected in the /input folder:
#load the image with pillow
#apply the crop_center and windowing functions as defined in your cygno_preprocessing module
#drop the absolute path from the file name to retrieve the "base file name" and its extension (check os.path.basename)
#store the preprocessed image in the /output folder, with the same "base name" as the original file;
#remove the original file (you may want to check the os.remove method)
#💡Hint. Your next cell may look like

#  for image_file in  # ... your call to glob method
#     # ... your preprocessing steps
#     # ... your procedure to store the file in /output
#     os.remove(image_file)

############### IMPORT LIBRARIES
import time
import numpy as np
import PIL
from glob import glob
from PIL import Image
import os
#p data/export/train data/input

############### PREPROCESSING PARAMETERS
crop_half_win = 64
x_min = 80 # windowing min brightness clip
x_max = 120 # windowing max brightness clip
input_data_folder_path = "/home/jovyan/data/input/*/*/*/*.png"
output_data_folder_path = "/home/jovyan/data/output"

############### FUNCTIONS DEFINITION
def windowing(figure, x_min, x_max):
    """Maps the pixel values from the interval [x_min, x_max] to [0, 1]"""
    rescaled = (figure - x_min)/(x_max - x_min)
    return np.clip(rescaled, 0, 1)

def crop_center(np_image, half_win=64):
    x0 = int(np_image.shape[0]/2)
    y0 = int(np_image.shape[1]/2)
    center_crop = np_image[x0 - half_win:x0 + half_win, y0 - half_win:y0 + half_win]
    return center_crop

############# PREPROCESSING
while True:
    time.sleep(10)
    input_files = glob(input_data_folder_path)
    print('input files:', input_files)
    for input_filename in input_files:
        image = Image.open(input_filename)
        np_image = np.array(image)
        processed_np_image = center_crop = crop_center(np_image, crop_half_win)
        processed_np_image = windowing(processed_np_image, x_min, x_max)
    
        output_filename = output_data_folder_path + '/' + os.path.basename(input_filename) #input_filename.replace("input", "output")
        Image.fromarray((255 * processed_np_image).astype(np.uint8)).save(output_filename)
        os.remove(input_filename)
    
