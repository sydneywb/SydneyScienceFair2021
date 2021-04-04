# importing the PSNR function and other packages
import sys
path = '/Users/sydneybadescu/Desktop/python_work/science_fair2021/functions_modules'
sys.path.append(path)

import numpy as np 
from PIL import Image
from cv2 import imread

from math import log10
def PSNR(original, compressed):
	mse = np.mean((original - compressed) ** 2)
	if mse == 0: # MSE is zero means no noise is present in the signal
				 # Therefore PSNR have no importance
		return 100
	max_pixel = 255.0
	psnr = 10 * log10((max_pixel)**2 / mse)
	return psnr

# working with numpy arrays
observed = np.ones((3,3))
predicted = np.zeros((3,3))

print('Observed:\n', observed)

observed[0][0] = 4
print(observed)

# looking at a real image
file = '/Users/sydneybadescu/Desktop/python_work/science_fair2021/cover_images/10cover.png'
edge = '/Users/sydneybadescu/Desktop/python_work/science_fair2021/stego_images/edge/10edge.png'
print(PSNR(imread(file), imread(edge)))
exit()

img = imread(file)
print(img.shape)
l, w = img.shape[0], img.shape[1]
for row in range(w):
	for col in range(l):
		pass






