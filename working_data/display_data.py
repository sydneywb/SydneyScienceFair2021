import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import json

# This program takes the data from 'format_data.json' and creates bar graphs to display my experiment results
# NOTE: I want to display my data so that shorter bars are not covered by taller ones

def bar_graph(dict, graph, y_label, x_label, title, ylim_bottom=None, custom_legend=None):
	# graph 
	for key, val in dict.items():
		sort_heights = sorted([height for height in val.keys()])[::-1]
		for height in sort_heights:
			color = val[height]
			graph.bar(key,float(height),color=f'tab:{color}', label=legend[color])

	graph.set_xlabel(x_label)
	graph.set_ylabel(y_label)
	graph.set_title(title)
	graph.set_ylim(bottom=ylim_bottom)
	graph.legend(handles=custom_legend)


# assigns each stego method to a color so that coloring is consistent
legend = {'blue':'lsb', 'orange':'edge', 'green':'noise', 'red':'color'}

with open('format_data.json') as f:
	data = json.load(f)
	psnr, cap, avg = data[0], data[1], data[2]

	# Creating a custom legend for my graphs
	legend_elements = [
		Patch(facecolor='tab:blue', label='LSB'),
		Patch(facecolor='tab:orange', label='Edge-Based'),
		Patch(facecolor='tab:green', label='Noise-Based'),
		Patch(facecolor='tab:red', label='Color-Based')
	]

	# PSNR Graph
	fig1, ax1 = plt.subplots()
	bar_graph(psnr, ax1, 'PSNR (dB)', 'Image Number', 'Comparing PSNR of Different Image Steganography Methods', ylim_bottom=42, custom_legend=legend_elements)

	# Capacity Graph
	fig2, ax2 = plt.subplots()
	bar_graph(cap, ax2, 'Capacity (number of pixels)', 'Image Number', 'Comparing Capacity of Different Image Steganography Methods', custom_legend=legend_elements)
	
	plt.show()
			





