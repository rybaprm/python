def preview_len_30_sumbol(string1):
	string = string1.replace('  ', ' ')
	string = string1.strip()
	if string1[29:30] == ' ' or string1[30:31] == ' ':
		preview_string=string1[0:30]
	else:	
		preview_string=string1[0:string1[0:30].rfind(' ')] + '...'
	return preview_string
		 
print(preview_len_30_sumbol('Split the string at the first occurrence of sep'))
print(preview_len_30_sumbol('The outermost leading and trailing chars argument values are stripped from the string'))
print(preview_len_30_sumbol('GitHub is built for collaboration. Set up an organization to improve the way your team works together, and get access to more features.'))
print(preview_len_30_sumbol('Using the Hello World guide, you’ll create a repository, start a branch, write comments, and open a pull request.'))
print(preview_len_30_sumbol('123 56789 123456 89 123 56789 123'))
print(preview_len_30_sumbol('123 56789 123456 89 123 567890 23'))
print(preview_len_30_sumbol('123 56789 123456 89 123 5678901 3'))
