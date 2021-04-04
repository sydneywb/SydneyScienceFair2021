from identifying_parts import *
from stego_encoders import PSNR
from cv2 import imread
from PIL import Image
import json

# This program generates the data for PSNR and character capacity then stores it in a JSON file

# list of all cover images
og_imgs = [f'{num}cover.png' for num in range(50)]

# dictionaries that store PSNR, px capacity, and averages data (will be loaded into JSON file)
psnr, cap, avg = {}, {}, {}

functions = {find_all:'lsb', find_edges:'edge', find_noise:'noise', find_blue:'color'}

# initialize values as lists for psnr and cap dictionaries
for val in functions.values():
	psnr[val] = []
	cap[val] = []

# store actual data in psnr and cap dictionaries
for img in og_imgs:
	
	img_num = int(img[:-9])
	og_img = imread(f'cover_images/{img}')

	for func, name in functions.items():
		# calculating px capacity
		capacity = func(Image.open(f'cover_images/{img}'))

		# calculating psnr
		stego = imread(f'stego_images/{name}/{img_num}{name}.png',1)
		psnr_val = PSNR(og_img, stego)

		psnr[name].append(float(psnr_val))
		cap[name].append(int(capacity))

	print('Finished', img + '...')

# store actual data in avg dictionary
for method in functions.values():
	# calculating psnr average
	psnr_list = psnr[method]
	psnr_avg = sum(psnr_list) / len(psnr_list)
	avg[f'{method}_psnr_avg'] = psnr_avg

	# calculating capacity average
	cap_list = cap[method]
	cap_avg = sum(cap_list) / len(cap_list)
	avg[f'{method}_cap_avg'] = cap_avg

with open('data.json','w') as f:
	json.dump([psnr,cap,avg], f)