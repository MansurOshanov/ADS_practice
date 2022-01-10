#Cracking the coding interview: Pseudo-code solution attempts:

#1.6
def compress_string(my_string):
	result = []
	previous_letter = my_string[0]
	count = 1
	for i, char in enumerate(my_string[1:]):
		if char == previous_letter:
			count += 1
		else:
			result.append(previous_letter)
			result.append(str(count))
			previous_letter = char
			count = 1
	result.append(previous_letter)
	result.append(str(count))
	compressed_string = "".join(result)
	if len(compressed_string) < len(my_string):
		return compressed_string
	return my_string

print(compress_string('aabcccccaa'))

