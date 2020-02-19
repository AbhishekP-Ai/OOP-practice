from PIL import Image
import os

class Imge(object):
	"""docstring for Image"""
	def __init__(self, path):
		#super(Image, self).__init__()
		self.path = path

	def get_image(self):
		image = Image.open(self.path)
		return image

	def get_path_info(self):
		filename, file_extension = os.path.splitext(self.path)
		print("File Extension: ",file_extension)
		splt = filename.split("-",2)
		magnification = splt[1]
		print("Magnification: ",magnification)
		split_for_date = filename.split("-",4)
		#print(split_for_date)
		for elements in split_for_date:
			#print(elements)
			date_time = elements[:-1].rsplit("-",3)
			time_split = elements[:-1].split("-",3)
		#print(time_split)
		date = date_time[0]
		print("Captured_date: ", date)
		time = time_split[-1]
		print("Captured_time: ", time)		
		return magnification,date,time

	def get_image_info(self):
		# dtype of image in PIL is not useful
		im = self.get_image()
		size = im.size
		print('Width: ', im.width)
		print('Height:', im.height)
		return size


img = Imge("/home/ilda/Desktop/003-100X-1-00DX-2019-12-02-16-55-49.jpg")
img.get_image()
img.get_path_info()
img.get_image_info()