from sf2021_functions import *
from PIL import Image, ImageFilter

# this program takes a given image and extracts the hidden message embedded in the edges
# NOTE: the original image AND the stego image are required inputs to extract the message

og_img = 'images_and_texts/pink_flower.png'
stego_image = 'images_and_texts/stego_edge_flower.png'

with Image.open(stego_image) as stego:

	img = Image.open(og_img)
	og_img_edge = img.convert('L').filter(ImageFilter.FIND_EDGES)

	grey_stego = stego.convert('L') # convert to greyscale
	
	px_og_edge = og_img_edge.convert('RGB').load()
	px_stego = stego.load()
	text_bin = ''
	for row in range(stego.size[1]):
		for col in range(stego.size[0]):
			if px_og_edge[col,row][0] > 30:
				blue_bin = decimal_to_binary(px_stego[col,row][2]) # convert blue value of stego image to binary
				text_bin += blue_bin[-1]

	text = bin_to_text(text_bin)
	print(text)
