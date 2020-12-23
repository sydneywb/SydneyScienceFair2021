import sys
sys.path.append('/Users/sydneybadescu/Desktop/python_work/science_fair2021')
"""
from sf2021_functions import *
from PIL import Image


# this was just to create a picture that is completely black
with Image.open('/Users/sydneybadescu/Desktop/python_work/science_fair2021/images_and_texts/pink_flower.png') as img:
	px = img.load()
	for row in range(img.size[1]):
		for col in range(img.size[0]):
			px[col,row] = (0,0,0)
	img.show()
	img.save('/Users/sydneybadescu/Desktop/black.png')


# modify the completely black image with hidden message
with Image.open('/Users/sydneybadescu/Desktop/black.png') as black:
	text = 'gocelebratesydney'*2757 + 'gocele'
	text_bin = text_to_bin(text)

	px = black.load()
	text_bin_indx = 0
	for row in range(black.size[1]):
		for col in range(black.size[0]):
			r, g, b = px[col,row][0], px[col,row][1], px[col,row][2]
			old_bbin = decimal_to_binary(b)

			new_bbin = binary_to_decimal(old_bbin[:-1] + text_bin[text_bin_indx])
			
			print(int(new_bbin))
			print(px[col,row])
			px[col,row] = (255, g, int(new_bbin))
			print(px[col,row])
			text_bin_indx += 1

	# black.show()
	black.save('/Users/sydneybadescu/Desktop/stego_black2.png')


# now extract message and see if it was embedded properly
with Image.open('/Users/sydneybadescu/Desktop/stego_black2.png') as stego:
	px = stego.load()
	for row in range(stego.size[1]):
		for col in range(stego.size[0]):
			print(px[col,row])

# this was for the edge-based image steganography
# it produces an image where the edge detection differences between the original and the stego are made red
og_edge = Image.open('images_and_texts/edge_circle.png').convert('RGB')
og_px = og_edge.load()
stego_px = edge_stego.load()

match, diff = 0, 0
for row in range(stego.size[1]):
	for col in range(stego.size[0]):
		if og_px[col,row] == stego_px[col,row]:
			match += 1
		else:
			diff += 1
			og_px[col,row] = (255,0,0)
og_edge.show()
og_edge.save('images_and_texts/throwsoff_edge_circle.png')
print(f'Matches: {match}, Differences: {diff}')
exit()
"""

