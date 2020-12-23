from PIL import Image
from sf2021_functions import *

# This program does basic LSB image steganography with a given image and message.

with Image.open('images_and_texts/pink_flower.png') as img:
    
    # open the text file with the secret message and read the content
    message = open('images_and_texts/moby_dick.txt')
    content = just_text(message.read())
    message.close()

    # convert the secret message into a string of binary numbers
    long_bin = text_to_bin(content)

    # check if message can fit in image and if not, notify the user
    num_of_px = img.size[0] * img.size[1]
    if len(long_bin) > num_of_px:
        print('The image does not have the capacity to hold your message,'
        f' so the message will be cut off after {int(num_of_px/8)} out of {len(content)} characters.')

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

    # img.show()
    img.save('images_and_texts/stego_flower.png')


