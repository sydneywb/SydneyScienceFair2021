
# STEPS:
# 1. Access each cover image
# 2. Create a stego image (with each method) that stores the same amount of text
# 3. Save the stego image
# 4. Access each stego image and calculate PSNR

import sys
sys.path.append('/Users/sydneybadescu/Desktop/python_work/science_fair2021/functions_modules')

from PIL import Image
from stego_encoders import *

path = '/Users/sydneybadescu/Desktop/python_work/science_fair2021/'
methods = {lsb:'lsb_const', edge:'edge_const', noise:'noise_const', color:'color_const'}
for img_num in range(50):
	og_img = path + f'cover_images/{img_num}cover.png'
	for method, name in methods.items():
		stego_save = f'const_stego/{img_num}_{name}.png'
		message = path + 'working_data/secret.txt'

		output = method(og_img, message)
		stego_img, cap = output[0], output[1]

		stego_img.save(stego_save)
		print(f"Finished Image {img_num}... ")
		print(cap)
