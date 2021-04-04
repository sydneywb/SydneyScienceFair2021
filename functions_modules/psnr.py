from math import log10, sqrt
import cv2
import numpy as np 

from stego_encoders import * # import PSNR()

# This program calculates the PSNR for a given original image and stego image.

og_img = 'images_and_texts/basic_lsb/pink_flower.png'
stego_img = 'images_and_texts/basic_lsb/stego_lsb_flower.png'


def main():
	original = cv2.imread(og_img)
	compressed = cv2.imread(stego_img, 1)
	value = PSNR(original, compressed)
	print(f"PSNR value is {value} dB")

if __name__ == '__main__':
	main()
