def string_from_some_sumbol_first_string_and_all_sumbol_second_string_duplicate(string1, string2):
	string = string1 + string2
	count_of_duplicate = 0
	for sumbol_index in range(len(string2)):
		if string.count(string2[sumbol_index]) == 2:
			count_of_duplicate += 1
	if count_of_duplicate == len(string2):
		print(f"You can make string from some sumbol in first string '{string1}' and all sumbol in second string '{string2}' with duplicate")
	else:
		print(f"You can't make string from some sumbol in first string '{string1}' and all sumbol in second string '{string2}' with duplicate")
	
string_from_some_sumbol_first_string_and_all_sumbol_second_string_duplicate('abc', 'dadebe')
string_from_some_sumbol_first_string_and_all_sumbol_second_string_duplicate('tac1', 'dadece1t')
string_from_some_sumbol_first_string_and_all_sumbol_second_string_duplicate('abc', 'adebe')
input()