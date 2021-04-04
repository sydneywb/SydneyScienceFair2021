from sf2021_functions import *
from PIL import Image, ImageFilter

# This program embeds a hidden message in the edges of an image

og_img = 'images_and_texts/edge/pink_flower_copy.png'
hidden_message = 'images_and_texts/moby_dick.txt'
edge_img = 'images_and_texts/edge/edge_flower.png'
stego_img = 'images_and_texts/edge/stego_edge_flower.png'

with Image.open(og_img) as img:

	# convert the image to greyscale
	img = img.convert('L')

	# detect edges in the image
	img = img.filter(ImageFilter.FIND_EDGES)

	# img.show()
	img.save(edge_img)

with Image.open(edge_img) as edge:
	edge = edge.convert('RGB') # convert the greyscale image back to RGB
	px = edge.load()

	# open the original image
	og_img = Image.open(og_img).convert('RGB')
	og_px = og_img.load()

	# the hidden message to be embedded in the image
	text = open(hidden_message).read()
	text_bin = text_to_bin(text)

	text_bin_indx = 0
	for row in range(edge.size[1]):
		for col in range(edge.size[0]):

			# since the image is in black and white, all of the pixels have the same R, G, and B values (ex: (38,38,38))
			# below, I identify the pixels that are colored lighter and thus are the ones identified as edges
			
			if px[col,row][0] > 30: # if the red value is greater than 30, so are the green and blue ones
				
				# access the blue value of the pixel and convert to binary
				blue_bin = decimal_to_binary(og_px[col,row][2])

				# alter the LSB of the blue value and convert to decimal
				new_blue = binary_to_decimal(blue_bin[:-1] + text_bin[text_bin_indx])
				
				og_px[col,row] = (og_px[col,row][0], og_px[col,row][1], new_blue)
				text_bin_indx += 1
				
	# notify user if the image does not have enough room to store the entire message
	text_indx = int(text_bin_indx/8)
	if len(text_bin) > text_bin_indx+1:
		print('The image does not have the capacity to hold your message,'
			f' so the message will be cut off after {text_indx} out of {len(text)} characters.')
		print(f"Here are the last 12 characters embedded: {bin_to_text(text_bin[text_indx*8-96:text_indx*8])}")

	og_img.save(stego_img)
	og_img.close()
	



