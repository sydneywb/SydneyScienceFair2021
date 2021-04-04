from PIL import Image, ImageEnhance, ImageFilter

og_img = '/Users/sydneybadescu/Desktop/python_work/science_fair2021/images_and_texts/pink_flower.png'
new_name = '/Users/sydneybadescu/Desktop/python_work/science_fair2021/images_and_texts/sharp_flower.png'
"""
with Image.open(og_img) as img: # this block creates and saves a sharpened image
	enhancer = ImageEnhance.Sharpness(img)
	sharp = enhancer.enhance(2)
	sharp.show()
	sharp.save(new_name)


# the sharp image looks the same as the original, so this is to check if they're actually identical
with Image.open(new_name) as sharp:
	og = Image.open(og_img)
	og_px, sharp_px = og.load(), sharp.load()
	same, diff = 0, 0
	for row in range(sharp.size[1]):
		for col in range(sharp.size[0]):
			if og_px[col,row] == sharp_px[col,row]:
				same += 1
			else:
				diff += 1
	print(f'Same: {same}, Different: {diff}')
"""

with Image.open(og_img) as img:
	blurred_img = img.filter(ImageFilter.GaussianBlur(1)) # only want to smooth a little or else edges get lost
	blurred_img.show()
	blurred_img.save('/Users/sydneybadescu/Desktop/python_work/science_fair2021/images_and_texts/blur_flower.png')

