from PIL import Image
from sf2021_functions import *

# This program takes in a stego image and produces the secret message.

with Image.open('images_and_texts/stego_flower.png') as stego_img:

    # access the blue value of each pixel in the image
    px, message_bin = stego_img.load(), ''

    message_indx = 0

    for row in range(stego_img.size[1]):
        for col in range(stego_img.size[0]):

            blue_bin = decimal_to_binary(px[col,row][2]) # convert the blue value from a decimal to binary number
            message_bin += blue_bin[-1] # take the last digit of the binary and concatenate it to a string

            message_indx += 1

    # iterate through the list of 8-bit binary numbers and convert each to a letter
    print(bin_to_text(message_bin))
