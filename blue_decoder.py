from sf2021_functions import *
from PIL import Image

# this program takes a given message and extracts the message hidden in the blue pixels
# NOTE: both the original and stego images are required inputs

og_img = 'images_and_texts/blue/mountain_lake.png'
hidden_message = 'images_and_texts/moby_dick.txt'
stego_img = 'images_and_texts/blue/stego_blue_lake.png'

with Image.open(stego_img) as stego:
	og_px = Image.open(og_img).load()
	stego_px = stego.load()

	text_bin = ''
	for row in range(stego.size[1]):
		for col in range(stego.size[0]):
			tup = og_px[col,row]
			if tup[2] > tup[1] and tup[2] > tup[0]:
				blue_bin = decimal_to_binary(stego_px[col,row][2])
				text_bin += blue_bin[-1]

	text = bin_to_text(text_bin)
	print('Extracted Message:', text)



