def string_first_letter_uppercase(string1):
	string_uppercase = ''
	for _ in string1.split():
		string_uppercase += _[0:1].upper() + _[1:] + ' '
	return string_uppercase
		 
print(string_first_letter_uppercase('the USA is a country comprising 50 states'))
