def string_contains_abc(string):
	if string.count('a') + string.count('b') + string.count('c') == len(string):
		if string.count('a') != 0 and string.count('b') != 0 and string.count('c') != 0:
			print(f"{string=} contains only sumbol 'a', 'b', 'c'")
		else:
			print(f"{string=} don't contains only sumbol 'a', 'b', 'c'")
	else:
		print(f"{string=} don't contains only sumbol 'a', 'b', 'c'")

string_contains_abc('aaaabbbbccc')
string_contains_abc('aaaasssssbbbbccc')
string_contains_abc('bbbbccc')
input()