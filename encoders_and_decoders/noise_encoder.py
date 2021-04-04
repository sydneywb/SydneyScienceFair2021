from sf2021_functions import *
from PIL import Image, ImageFilter

# This program embeds a hidden message in the textured regions of an image


og_img = 'images_and_texts/texture/japan_autumn.png'
hidden_message = 'images_and_texts/moby_dick.txt'
blur_save = 'images_and_texts/texture/blur_japan.png'
stego_img = 'images_and_texts/texture/stego_texture_japan.png'

with Image.open(og_img) as img:

	# open the file with the message and convert to binary
	text = open(hidden_message).read()
	text_bin = text_to_bin(text)

	# smooth the image slightly to eliminate noise, then compare to original to identify noisy regions
	blurred_img = img.filter(ImageFilter.GaussianBlur(0.3))
	blurred_img.save(blur_save)

	og_px, blur_px = img.load(), blurred_img.load()
	text_bin_indx = 0
	for row in range(img.size[1]):
		for col in range(img.size[0]):
			if og_px[col,row] != blur_px[col,row]:
				blue_bin = decimal_to_binary(og_px[col,row][2])
				new_blue = blue_bin[:-1] + text_bin[text_bin_indx]
				og_px[col,row] = (og_px[col,row][0], og_px[col,row][1], binary_to_decimal(new_blue))
				text_bin_indx += 1

	# notify user if the image does not have enough room to store the entire message
	text_indx = int(text_bin_indx/8)
	if len(text) > text_indx+1:
		print('The image does not have the capacity to hold your message,'
			f' so the message will be cut off after {text_indx} out of {len(text)} characters.')
		print(f"Here are the last 12 characters embedded: {bin_to_text(text_bin[text_indx*8-96:text_indx*8])}")

	img.show()
	img.save(stego_img)

