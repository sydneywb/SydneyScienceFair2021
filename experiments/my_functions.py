# UPDATE: I can convert from rgb to binary without converting to hex in between.
# This is where I developed a lot of my functions

def rgb_to_hex(rgb_tuple):

	# initialize hex characters, exponent for 16, and final list of hex numbers
	hexa_alpha, exp, hex_list = '0123456789ABCDEF', 0, []

	# operate on each r, g, and b value one at a time
	for color in rgb_tuple:

		# find how many digits the hexadecimal number will need
		while (16**exp) < color:
			exp += 1
		hexa = ['0' for i in range(exp)]

		# change each '0' to the correct digit
		for char in range(len(hexa)):
			exp -= 1

			# indx is how many times 16**exp goes into this r,g,or b value
			indx = color//(16**exp)
			hexa[char] = hexa_alpha[indx]
			color -= indx * 16**exp

		# convert the hex number to a string then store it in final hex_list
		string = ''
		for char in hexa:
			string += char
		hex_list.append(string)
	
	hex_tup = tuple(hex_list)
	return hex_tup
px = rgb_to_hex((231, 174, 171))

def rgb_to_bin(rgb_tuple):

	# initialize bin characters, exponent for 2, and final list of bin numbers
	bin_alpha, exp, bin_list = '01', 0, []

	# operate on each r, g, and b value one at a time
	for color in rgb_tuple:

		# find how many digits the binary number will need
		while (2**exp) < color:
			exp += 1
		binary = ['0' for i in range(exp)]

		# change each '0' to the correct digit
		for char in range(len(binary)):
			exp -= 1

			# indx is how many times 2**exp goes into this r,g,or b value
			indx = color//(2**exp)
			binary[char] = bin_alpha[indx]
			color -= indx * 2**exp

		# convert the bin number to a string then store it in final bin_list
		string = ''
		for char in binary:
			string += char
		bin_list.append(int(string))
	
	bin_tup = tuple(bin_list)
	return bin_tup
bin_px = rgb_to_bin((231, 174, 171))

def decimal_to_binary(decimal_num):
	bin_alpha, exp, bin_list = '01', 0, []
	while (2**exp) < decimal_num:
		exp += 1
	binary = ['0' for i in range(exp)]
	for char in range(len(binary)):
		exp -= 1
		indx = decimal_num//(2**exp)
		binary[char] = bin_alpha[indx]
		decimal_num -= indx * 2**exp
	string = ''
	for char in binary:
		string += char
	return string

def remove_spaces(text):
	word_list, new_text = text.split(), ''
	for word in word_list:
		new_text += word
	return new_text
no_spaces = remove_spaces('why hello there')

def text_to_bin(text):
	# Unicode 8-bit, A-Z -> 65-90
	unicode_nums, alpha, alpha_to_uni = [i for i in range(65,91)], 'abcdefghijklmnopqrstuvwxyz', {}
	for letter in range(len(alpha)):
		alpha_to_uni[alpha[letter]] = unicode_nums[letter] 
	text, text_bin = remove_spaces(text.lower()), []
	for char in text:
		text_bin.append(decimal_to_binary(alpha_to_uni[char]))
	return text_bin
text_bin = text_to_bin('no more secrets')

def binary_to_decimal(binary_str):
	reverse_bin, decimal = binary_str[::-1], 0
	for indx in range(len(reverse_bin)):
		decimal += int(reverse_bin[indx]) * (2**indx)
		# print(f"{reverse_bin[indx]} * 2**{indx} = {int(reverse_bin[indx]) * (2**indx)}")
	return decimal
decimal_int = binary_to_decimal('1000000')

def just_text(string):
	alpha, new_string = 'abcdefghijklmnopqrstuvwxyz', ''
	for char in string:
		if char in alpha:
			new_string += char
	return new_string
just_text = just_text('/this67  @"should j+ust,be;t2ext')

def bin_to_text(binary):
	# separate the binary of the message into groups of 8 bits
	bits = []
	while binary:
		bits.append(binary[:8])
		binary = binary[8:]
	# Unicode 8-bit, A-Z -> 65-90
	unicode_nums, alpha, alpha_to_uni = [i for i in range(65,91)], 'abcdefghijklmnopqrstuvwxyz', {}
	for letter in range(len(alpha)):
		alpha_to_uni[unicode_nums[letter]] = alpha[letter]
	text = ''
	for bit in bits:
		char = alpha_to_uni[binary_to_decimal(bit)]
		text += char
	return text
print(bin_to_text('1000001'))



















