from sf2021_functions import *
from PIL import Image, ImageFilter

# this program takes a given image and extracts the hidden message embedded in the textured regions
# NOTE: both the original image AND the stego image are required inputs

og_img = 'images_and_texts/japan_autumn.png'
stego_img = 'images_and_texts/stego_texture_japan.png'

with Image.open(stego_img) as stego:
	og = Image.open(og_img)
	blur = og.filter(ImageFilter.GaussianBlur(0.3))

	blur_px, stego_px, og_px = blur.load(), stego.load(), og.load()
	text_bin = ''
	for row in range(stego.size[1]):
		for col in range(stego.size[0]):
			if og_px[col,row] != blur_px[col,row]:
				blue_bin = decimal_to_binary(stego_px[col,row][2])
				text_bin += blue_bin[-1]

	text = bin_to_text(text_bin)

	print('Extracted Message:', text)
