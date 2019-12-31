def string_replace_abc_www_or_add_to_end_zzz(string):
	if string.count('abc', 0, 3) !=0:
		string = string.replace('abc', 'www', 1)
	else:
		string+= 'zzz'
	print(string)
	
string_replace_abc_www_or_add_to_end_zzz('abcabcabc')
string_replace_abc_www_or_add_to_end_zzz('bcabcabc')
input()