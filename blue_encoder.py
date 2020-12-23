from sf2021_functions import *
from PIL import Image

# this program embeds a hidden message in the blue-colored pixels of an image

og_img = 'images_and_texts/blue/mountain_lake.png'
hidden_message = 'images_and_texts/moby_dick.txt'

with Image.open(og_img) as img:

	# open the file with the hidden message and convert to binary
	text = open(hidden_message).read()
	text_bin = text_to_bin(text)

	px = img.load()
	text_bin_indx = 0
	for row in range(img.size[1]):
		for col in range(img.size[0]):
			tup = px[col,row]
			if tup[2] > tup[0] and tup[2] > tup[1]:
				blue_bin = decimal_to_binary(tup[2])
				new_blue = binary_to_decimal(blue_bin[:-1] + text_bin[text_bin_indx])
				px[col,row] = (tup[0], tup[1], new_blue)
				text_bin_indx += 1
	
	# notify user if the image does not have enough room to store the entire message
	text_indx = int(text_bin_indx/8)
	if len(text) > text_indx+1:
		print('The image does not have the capacity to hold your message,'
			f' so the message will be cut off after {text_indx} out of {len(text)} characters.')
		print(f"Here are the last 12 characters embedded: {bin_to_text(text_bin[text_indx*8-96:text_indx*8])}")
	
	img.show()
	img.save('images_and_texts/stego_blue_lake.png')