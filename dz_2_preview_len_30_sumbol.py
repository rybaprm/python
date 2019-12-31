def preview_len_30_sumbol(string1):
	string = string1.replace('  ', ' ')
	string=string1.strip()
	if string1[29:30] ==' ' or string1[30:31] ==' ':
		preview_string=string1[0:30]
	else:	
		preview_string=string1[0:string1[0:30].rfind(' ')] + '...'
	return preview_string
		 
print(preview_len_30_sumbol('Split the string at the first occurrence of sep'))
print(preview_len_30_sumbol('The outermost leading and trailing chars argument values are stripped from the string'))
print(preview_len_30_sumbol('Split the string at the firs_t occurrence of sep'))
print(preview_len_30_sumbol('Split the string at the firs__t occurrence of sep'))