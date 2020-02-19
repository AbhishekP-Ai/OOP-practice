# /bin/python utf-8 

import cv2
import numpy as np 
from PIL import Image 
import os 


class ImageRead:
    def __init__(self, path):
        self.path = path

    def image_read(self):
        blood_image = Image.open(self.path)   
        return blood_image

class ImageMetaData(ImageRead):
    def __init__(self, path):
        super().__init__(path)
        self.path = path
    def getImageLocation(self):
        print("Image is location at {}".format(self.path))
    def getImageExtension(self):
        valid_extensions = ['JPG','JPEG','PNG','TIFF']
        image = self.image_read()
        image_extension = image.format
        print(image_extension)
        
    def getImageChannel(self):
        image = self.image_read()
        print(image.mode)
        
    def getImageSize(self):
        image = self.image_read()
        print(image.size)
        
    def getImageInfo(self):
        image = self.image_read()
        image_info = image.info 
        for key,value in image_info.items():
            if key == 'dpi':
                print("Image DPI is {}".format(value))
                
    def getImageShape(self):
        image = self.image_read()
        height = image.height
        width = image.width
        print("Image Height is {}, and Widht is {}".format(height, width))
        
    def getImageMagnification(self):
        image_location = self.path 
        base_name = os.path.basename(image_location)
        base = base_name.split(".")
        image_magnification = base[0].split("-")
        print("Image magnification is {}".format(image_magnification[1]))
        
    
    def getMetaDataofImage(self):
        self.getImageLocation()
        self.getImageChannel()
        self.getImageInfo()
        self.getImageExtension()
        self.getImageMagnification()
        self.getImageShape()
        self.getImageSize()



path = "/home/aimd-01/Desktop/003-100X-1-00DX-2020-02-03-15-05-16.jpg"
image = ImageRead(path)
image_read = image.image_read()
image_object = ImageMetaData(path)
image_metadata = image_object.getMetaDataofImage()