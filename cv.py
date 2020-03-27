import os
from PIL import Image

image_file = Image.open('caroline.jpg')
image_file = image_file.convert('L') #onvert image to black and whtite
image_file.save('result.png')


for file in os.listdir('.'):
	if file.endswith('.jpg'):
		print(file)