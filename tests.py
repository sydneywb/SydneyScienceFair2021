from PIL import Image
from sf2021_functions import *

# changes blue value to 0 in top section of image
with Image.open('images_and_texts/pink_flower.jpg') as img:
    for row in range(500):
        for col in range(500):
            px = img.load()
            px_list = list(px[row, col])
            r, g = px_list[0], px_list[1]
            px[row, col] = (r, g, 0)
    img.show()

# Can I read a file then close it after assigning its contents to a variable? YES!
with open('images_and_texts/moby_dick.txt') as f:
    content = f.read()
    f.close()
    print(content)

# How does the exit() function work?
if 0 == 0:
    print('Hello')
    exit()
print('Goodbye')

# How can I separate a long binary number into groups of 8 bits? (It's easier to see the groups as 8-letter words)
text = 'absolutemountainsentencerelationrationedasteroidtoenails'
separated_bits = []
while text:
    separated_bits.append(text[:8])
    text = text[8:]
print(separated_bits)

# Why is the message binary I extract from the stego image in lsd_decoder different than the binary I put in?
# take a short message, use your function to convert it to binary, then use the other function to take it out of binary and see if the message is preserved
text = 'nomoresecrets'
binary, bits, extract = text_to_bin(text), [], ''
while binary:
    bits.append(binary[:8])
    binary = binary[8:]
for bit in bits:
    extract += bin_to_text(bit)
print(extract)

with Image.open('images_and_texts/pink_flower.jpg') as og_img:
    px = og_img.load()
    for row in range(og_img.size[1]):
        for col in range(og_img.size[0]):
            print('OG BLUE DEC:', px[col,row][2])
with Image.open('images_and_texts/stego_flower.jpg') as stego_img:
    px = stego_img.load()
    for row in range(stego_img.size[1]):
        for col in range(stego_img.size[0]):
            print('STEGO BLUE DEC:', px[col,row][2])


# .getdata() versus .load() methods?
with Image.open('images_and_texts/pink_flower.jpg') as img:
    datas = img.getdata()
    for each in datas:
        print(each)
