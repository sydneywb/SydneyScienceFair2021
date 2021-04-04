"""
Q: I need to see if my computer can handle processing lots of data
and then put it into an image. If not, I will need a raspberry pi for additional CPU
A: Running the code in Visual Studio Code causes the window to stop responding, but it is
able to process the text when I run the code in terminal. No raspberry pi needed!
"""
def just_text(string):
	# NOTE: This function rids the given string of numbers, punctuation, spaces, and special characters
	alpha, new_string = 'abcdefghijklmnopqrstuvwxyz', ''
	for char in string.lower():
		if char in alpha:
			new_string += char
	return new_string
with open('images_and_texts/moby_dick.txt') as f:
    text = f.read()
    print(just_text(text))
    
