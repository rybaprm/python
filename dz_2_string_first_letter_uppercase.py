def string_first_letter_uppercase(string1):
	string_uppercase = ''
	for word_in_string in string1.split():
		string_uppercase += word_in_string[0:1].upper() + word_in_string[1:] + ' '
	return string_uppercase
		 
print(string_first_letter_uppercase('the USA is a country comprising 50 states'))
