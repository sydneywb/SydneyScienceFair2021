import json

# This program formats the data from 'data.json' to get it ready to be displayed as a bar graph

with open('data.json') as f:
	data = json.load(f)
	psnr, cap, avg = data[0], data[1], data[2]

	format_psnr, format_cap = {}, {}
	values = ['blue', 'orange', 'green', 'red']
	for img_num in range(50):
		keys_psnr = [psnr[name][img_num] for name in psnr.keys()] # heights of bars for that column
		keys_cap = [cap[name][img_num] for name in cap.keys()]

		val_psnr, val_cap = {}, {}
		for indx in range(4):
			val_psnr[keys_psnr[indx]] = values[indx]
			val_cap[keys_cap[indx]] = values[indx]

		format_psnr[img_num] = val_psnr
		format_cap[img_num] = val_cap
	with open('format_data.json', 'w') as f_out:
		json.dump([format_psnr, format_cap, avg], f_out)