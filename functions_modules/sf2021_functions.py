
# This module contains all of my functions for my 2021 science fair project.

def remove_spaces(text):
	word_list, new_text = text.split(), ''
	for word in word_list:
		new_text += word
	return new_text

def decimal_to_binary(decimal_num):
    bin_alpha, exp, bin_list = '01', 0, []
    while (2**exp) <= decimal_num:
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
    while len(string) < 8:
        string = '0' + string
    return string

def text_to_bin(text):
	# Unicode 8-bit, A-Z -> 65-90
	unicode_nums, alpha, alpha_to_uni = [i for i in range(65,91)], 'abcdefghijklmnopqrstuvwxyz', {}
	for letter in range(len(alpha)):
		alpha_to_uni[alpha[letter]] = unicode_nums[letter] 
	text, list_text_bin, str_text_bin = just_text(text.lower()), [], ''
	for char in text:
		list_text_bin.append(decimal_to_binary(alpha_to_uni[char]))
	for letter in list_text_bin:
		for digit in letter:
			str_text_bin += digit
	return str_text_bin

def binary_to_decimal(binary_str):
	reverse_bin, decimal = binary_str[::-1], 0
	for indx in range(len(reverse_bin)):
		decimal += int(reverse_bin[indx]) * (2**indx)
	return decimal

def just_text(string):
	# NOTE: This function rids the given string of numbers, punctuation, spaces, and special characters
	alpha, new_string = 'abcdefghijklmnopqrstuvwxyz', ''
	for char in string.lower():
		if char in alpha:
			new_string += char
	return new_string

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
	if len(bits[-1]) < 8:
		last = bits.pop()
	text = ''
	for bit in bits:
		char = alpha_to_uni[binary_to_decimal(bit)]
		text += char
	return text
