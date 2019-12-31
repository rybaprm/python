import string
import random
def string_three_elements_alphabetical_raddom_middle(string1):
	list_string=[]
	for element_index in range(int(len(string1)/3)):
		list_random_sumbol=string.ascii_lowercase + string.digits
		list_random_sumbol=list_random_sumbol.replace(string1[element_index*3:element_index*3+1],'')
		list_random_sumbol=list_random_sumbol.replace(string1[element_index*3+2:element_index*3+3],'')
		list_string.append(string1[element_index*3:element_index*3+1] + random.choice(list_random_sumbol) + string1[element_index*3+2:element_index*3+3])
	list_string.sort()
	return list_string
		 
print(string_three_elements_alphabetical_raddom_middle('string'))
print(string_three_elements_alphabetical_raddom_middle('myhomeqee'))