from PIL import Image, ImageFilter

# This module contains functions that idenify edges, noise, and blue regions in images
# Each functions returns a number that is the # of pixels of the specified type

def find_all(img):
	size = img.size[1] * img.size[0]
	return size

def find_edges(img):
	edge = img.convert('L').filter(ImageFilter.FIND_EDGES)
	px, count = edge.load(), 0
	for row in range(img.size[1]):
		for col in range(img.size[0]):
			if px[col,row] > 30:
				count += 1
	return count

def find_noise(img):
	blur = img.filter(ImageFilter.GaussianBlur(0.3))
	og_px, blur_px = img.load(), blur.load()
	count = 0
	for row in range(img.size[1]):
		for col in range(img.size[0]):
			if og_px[col,row] != blur_px[col,row]:
				count += 1
	return count

def find_blue(img):
	px, count = img.load(), 0
	for row in range(img.size[1]):
		for col in range(img.size[0]):
			r, g, b = px[col,row][0], px[col,row][1], px[col,row][2]
			if b > g and b > r:
				count += 1
	return count