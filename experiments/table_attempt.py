import os
from stego_encoders import *
from cv2 import imread
from tkinter import *

cover_imgs_folder = 'cover_images'

# List of 50 images to be used as cover images
images = [file for file in os.listdir(cover_imgs_folder)]
count = len(images)

root = Tk('Effectiveness of Different Adaptive Image Steganography Methods')
# Set up for the data table
Label(root,text='Image Steganography Method',borderwidth=.5,relief='solid').grid(row=0,column=0,columnspan=8,sticky='nsew')

Label(root,text='Basic LSB',borderwidth=.5,relief='solid').grid(row=1,column=0,columnspan=2,sticky='nsew')
Label(root,text='Edge-Based',borderwidth=.5,relief='solid').grid(row=1,column=2,columnspan=2,sticky='nsew')
Label(root,text='Noise-Based',borderwidth=.5,relief='solid').grid(row=1,column=4,columnspan=2,sticky='nsew')
Label(root,text='Color-Based',borderwidth=.5,relief='solid').grid(row=1,column=6,columnspan=2,sticky='nsew')

for i in range(0, 8, 2): Label(root,text='PSNR (dB)',borderwidth=.5,relief='solid').grid(row=2,column=i,sticky='nsew')
for i in range(1, 9, 2): Label(root,text='Capacity (# of characters)',borderwidth=.5,relief='solid').grid(row=2,column=i,sticky='nsew')

Label(root,text='Averages',borderwidth=.5,relief='solid').grid(row=count+3,column=0,sticky='nsew',columnspan=8)

# Using Moby Dick as hidden message to be embedded in cover image
hidden_message = 'images_and_texts/moby_dick.txt'

functions_list = {lsb:[0,'lsb'], edge:[2,'edge'], noise:[4,'noise'], color:[6,'color']}
storage = {
	'lsb_psnr':[], 'lsb_capacity':[],
	'edge_psnr':[], 'edge_capacity':[],
	'noise_psnr':[], 'noise_capacity':[],
	'color_psnr':[], 'color_capacity':[]
}

for og_img in images:
	img_num = int(og_img[:-9])
	for func in functions_list.keys():

		output = func(f'{cover_imgs_folder}/{og_img}', hidden_message)

		name, col = functions_list[func][1], functions_list[func][0]

		stego_save = f'stego_images/{name}/{img_num}{name}.png'
		output[0].save(stego_save)

		psnr, capacity = PSNR(imread(f'{cover_imgs_folder}/{og_img}'), imread(stego_save,1)), output[1]
		storage[f'{name}_psnr'].append(float(psnr))
		storage[f'{name}_capacity'].append(int(capacity))
		print(f'{stego_save}, PSNR: {psnr} dB, Capacity: {capacity}')

		psnr_label = Label(root,text=str(psnr),borderwidth=.5,relief='solid').grid(row=img_num+3,column=col,sticky='nsew')
		capacity_label = Label(root,text=str(capacity),borderwidth=.5,relief='solid').grid(row=img_num+3,column=col+1,sticky='nsew')

for func in functions_list:
	name, col = functions_list[func][1], functions_list[func][0]

	psnr_list, capacity_list = storage[f'{name}_psnr'], storage[f'{name}_capacity']
	psnr_avg = sum(psnr_list) / len(psnr_list)
	capacity_avg = sum(capacity_list) / len(capacity_list)

	Label(root,text=psnr_avg,borderwidth=.5,relief='solid').grid(row=count+4,column=col,sticky='nsew')
	Label(root,text=capacity_avg,borderwidth=.5,relief='solid').grid(row=count+4,column=col+1,sticky='nsew')


root.mainloop()









