from sf2021_functions import *
from PIL import Image, ImageFilter
import numpy as np 
from math import log10

# Each function in this module performs a different type of adaptive image steganography
# Inputs: original image and hidden message (directory path)
# Outputs: stego image and capacity
# The outputs of each function can be used to find capacity and PSNR for each steganography method

def lsb(og_img, hidden_message):
	with Image.open(og_img) as img:
	    
	    # open the text file with the secret message and read the content
	    message = open(hidden_message)
	    content = just_text(message.read())
	    message.close()

	    # convert the secret message into a string of binary numbers
	    long_bin = text_to_bin(content)

	    num_of_px = img.size[0] * img.size[1]
	    char_capacity = int(num_of_px/8)

	    # access the blue value of each pixel and convert it to binary
	    long_bin_indx, px = 0, img.load()
	    for row in range(img.size[1]):
	        for col in range(img.size[0]):
	            # stop editing the pixels when the entire message has been embedded (for if the message is too short)
	            if long_bin_indx >= len(long_bin):
	                break

	            px_tup = px[col, row]
	            px_bbin = decimal_to_binary(px_tup[2])

	            px_bbin = px_bbin[:-1] + long_bin[long_bin_indx] # change the LSB according to secret message
	            new_blue = binary_to_decimal(px_bbin) # change binary back to decimal to be read into RGB for image
	            
	            r, g = px_tup[0], px_tup[1]
	            px[col, row] = (r, g, new_blue) # change blue value to new one

	            long_bin_indx += 1

	    return [img, char_capacity]

def edge(og_img, hidden_message):
	with Image.open(og_img) as img:

		# convert the image to greyscale
		img = img.convert('L')

		# detect edges in the image
		edge = img.filter(ImageFilter.FIND_EDGES)

		# convert the greyscale image back to RGB
		edge = edge.convert('RGB')
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
					if text_bin_indx >= len(text_bin):
						break
					# access the blue value of the pixel and convert to binary
					blue_bin = decimal_to_binary(og_px[col,row][2])

					# alter the LSB of the blue value and convert to decimal
					new_blue = binary_to_decimal(blue_bin[:-1] + text_bin[text_bin_indx])
					
					og_px[col,row] = (og_px[col,row][0], og_px[col,row][1], new_blue)
					text_bin_indx += 1
					
		text_indx = int(text_bin_indx/8)

		return [og_img, text_indx]
		og_img.close()

def noise(og_img, hidden_message):
	with Image.open(og_img) as img:

		# open the file with the message and convert to binary
		text = open(hidden_message).read()
		text_bin = text_to_bin(text)

		# smooth the image slightly to eliminate noise, then compare to original to identify noisy regions
		blurred_img = img.filter(ImageFilter.GaussianBlur(0.3))

		og_px, blur_px = img.load(), blurred_img.load()
		text_bin_indx = 0
		for row in range(img.size[1]):
			for col in range(img.size[0]):
				if og_px[col,row] != blur_px[col,row]:
					if text_bin_indx >= len(text_bin):
						break
					blue_bin = decimal_to_binary(og_px[col,row][2])
					new_blue = blue_bin[:-1] + text_bin[text_bin_indx]
					og_px[col,row] = (og_px[col,row][0], og_px[col,row][1], binary_to_decimal(new_blue))
					text_bin_indx += 1

		text_indx = int(text_bin_indx/8)
		return [img, text_indx]

def color(og_img, hidden_message):
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
					if text_bin_indx >= len(text_bin):
						break
					blue_bin = decimal_to_binary(tup[2])

					new_blue = binary_to_decimal(blue_bin[:-1] + text_bin[text_bin_indx])
					px[col,row] = (tup[0], tup[1], new_blue)
					text_bin_indx += 1
		
		text_indx = int(text_bin_indx/8)

		return [img, text_indx]

def PSNR(original, stego):
	mse = np.mean((original - stego) ** 2)
	if mse == 0: # MSE is zero means no noise is present in the signal
				 # Therefore PSNR have no importance
		return 100
	max_pixel = 255.0
	psnr = 10 * log10((max_pixel)**2 / mse)
	return psnr


