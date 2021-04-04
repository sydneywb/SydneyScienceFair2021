from tkinter import *
import json
import matplotlib.pyplot as plt 

# This program displays the averages of the data as a table then as a graph

# -------------------------------------------------------------------------
# NOTE: I actually ended up using Google Sheets to make my table and graphs
# -------------------------------------------------------------------------

def label_maker(text, row, col, columnspan=1, color='white'):
	# Creates a label with my desired formatting so that I don't have to type details multiple times
	Label(root, text=text, borderwidth=0.5, relief='solid', bg=color).grid(row=row, column=col, sticky='nsew', columnspan=columnspan)


colors = {'LSB':'#448BBD', 'Edge':'#F39739', 'Noise':'#59A84A', 'Color':'#CF4B3E'}
with open('working_data/format_data.json') as f:
	data = json.load(f)
	avg = data[2]
	
	# TABLE
	root = Tk()
	label_maker('Averages', 0, 0, 2)
	row = 1
	for key, val in avg.items():

		# LABEL
		text = key[:-4].split('_')

		if text[0] == 'lsb': text[0] = 'LSB'
		else: text[0] = text[0].title()

		if text[1] == 'psnr': text[1] = 'PSNR'
		else: text[1] = 'Capacity'

		color = colors[text[0]]
		text = text[0] + ' ' + text[1]
		label_maker(text, row, 0, color=color)

		# NUMBER
		label_maker(round(val, 2), row, 1, color=color)
		row += 1

	root.mainloop()
	
	# GRAPH
	print(avg)



