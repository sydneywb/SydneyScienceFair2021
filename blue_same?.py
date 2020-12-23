from PIL import Image

# this program finds the blue pixels in the original and the blue in the stego
# then compares them. RESULT: blue in original and stego are different

og_img = 'images_and_texts/blue/mountain_lake.png'
stego_img = 'images_and_texts/blue/stego_blue_lake.png'

with Image.open(stego_img) as stego:

	og_img = Image.open(og_img)
	og = og_img.load()
	for row in range(stego.size[1]):
		for col in range(stego.size[0]):
			tupp = og[col,row]
			if tupp[2] > tupp[1] and tupp[2] > tupp[0]:
				og[col,row] = (0,0,255)
			else:
				og[col,row] = (0,0,0)

	px = stego.load()
	for row in range(stego.size[1]):
		for col in range(stego.size[0]):
			tup = px[col,row]
			if tup[2] > tup[1] and tup[2] > tup[0]:
				px[col,row] = (0,0,255)
			else:
				px[col,row] = (0,0,0)

	for row in range(stego.size[1]):
		for col in range(stego.size[0]):
			if og[col,row] != px[col,row]:
				og[col,row] = (255,255,0)
			else:
				og[col,row] = (0,0,0)
	og_img.show()
	og_img.save('images_and_texts/blue/blue_not_same.png')