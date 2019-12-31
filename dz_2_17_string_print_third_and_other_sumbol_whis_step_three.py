def string_print_third_and_other_sumbol_whis_step_three(string):
	string_to_print=''
	for sumbol_index in range(2,len(string),3):
		string_to_print += string[sumbol_index] + ' ' 
	print(f'{string=} third and other sumbol whis step three = {string_to_print}')
	
string_print_third_and_other_sumbol_whis_step_three('ab3ab6ab9ab')
string_print_third_and_other_sumbol_whis_step_three('ab3ab6ab9ab2ab5a')
input()