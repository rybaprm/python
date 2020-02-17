def string_sorted_word_alphabetical(string):
	while string.count('  '):
		string = string.replace('  ', ' ')
	list_string = sorted(string.split())
	string = ''
	for item in list_string:
		string += item + ' '
	list_string.clear()
	print(string)
	
string_sorted_word_alphabetical('big apple tree      under     dog')
input()