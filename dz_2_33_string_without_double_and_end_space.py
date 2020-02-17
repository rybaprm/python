def string_without_double_and_end_space(string):
	while string.count('  '):
		string = string.replace('  ', ' ')
	
	string = string.strip()
	print(string)

string_without_double_and_end_space('   home        work          home        work          home        work          home        work       ')
input()