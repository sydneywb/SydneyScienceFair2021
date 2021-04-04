from sf2021_functions import *
from PIL import Image

# This program does basic LSB image steganography with a given image and message.

cover_img = 'images_and_texts/basic_lsb/pink_flower.png'
hidden_message = 'images_and_texts/moby_dick.txt'
stego_save = 'images_and_texts/basic_lsb/stego_lsb_flower.png'

with Image.open(cover_img) as img:
    
    # open the text file with the secret message and read the content
    message = open(hidden_message)
    content = just_text(message.read())
    message.close()

    # convert the secret message into a string of binary numbers
    long_bin = text_to_bin(content)

    # check if message can fit in image and if not, notify the user
    num_of_px = img.size[0] * img.size[1]
    text_indx = int(num_of_px/8)
    if len(long_bin) > num_of_px:
        print('The image does not have the capacity to hold your message,'
        f' so the message will be cut off after {text_indx} out of {len(content)} characters.')
        print('Here are the last 12 characters embedded:', bin_to_text(long_bin[text_indx*8-96:text_indx*8]))

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

    img.save(stego_save)
