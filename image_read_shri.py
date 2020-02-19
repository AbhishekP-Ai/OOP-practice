

import os
# Function to rename multiple files
import cv2

'''
############## WITHOUT Instance attributes  ###############################################

class Image:
   #new_path = "/home/shri/Desktop/data/AIMD_SRMC_28_11_2019_PBS_0041-001-100X.jpg"
  
   def image_name(self, path): # note that the first argument is self
      self.path = path # access the class attribute with the self keyword
      print(path)
      image = cv2.imread(path)
      print(image.shape)

image =  Image()
print(image.image_name('/home/shri/Desktop/data/AIMD_SRMC_28_11_2019_PBS_0041-001-100X.jpg'))

###########################################################################################
'''
import re 
class Image:
   def __init__(self, path):
      self.path = path
      image = cv2.imread(self.path)
      self.image = image


   def image_read(self):
      print(self.image)
   
   def image_ext(self):
      path_list = self.path.split(os.sep)
      i_name  = path_list[-1]
      extension = i_name.split('.')
      print('Image format : ', extension[-1])

   def image_channel(self):
      print('Total image channels :', self.image.shape[-1])
      if self.image.shape[-1] == 3 :
         print("Sequence of channel is(OpenCV): B G R")
      else:
         print("Image is gray scale")

   def image_shape(self):
      print('Total image height: ', self.image.shape[0])
      print('Total image width: ', self.image.shape[1])
      print('Total image channel :', self.image.shape[2])

   def image_size(self):
      print('Total image size ', self.image.size)

   def image_date(self):
      path_list = self.path.split(os.sep)
      i_name  = path_list[-1]
      split = i_name.split('-')
      join = '-'.join(split[4:7])
      print("Image captuing date :",join) 

   def image_magnification(self):
      path_list = self.path.split(os.sep)
      i_name  = path_list[-1]
      split = i_name.split('-')
      print("Image magification :",split[1]) 

   def image_time(self):
      path_list = self.path.split(os.sep)
      i_name  = path_list[-1]
      split = i_name.split('-')
      time  = split[6:9]
      split2 = split[9].split('.')
      time.append(split2[0])
      time = '-'.join(time)
      print("Image captuing time :",time) 


i1 = Image('/home/shri/Desktop/003-100X-1-00DX-2020-02-03-15-05-16.jpg')
i1.image_size()

