def string_contains_plus_minus(string):
	plus_minus_count = string.count('-') + string.count('+')
	plus_minus_before_zero_count = string.count('-0') + string.count('+0')
	print(f"{string=} contains {plus_minus_count} sumbols '+' and '-'")
	print(f" and after {plus_minus_before_zero_count} of them set '0'")

string_contains_plus_minus('-------0-0-0-0-0+++++++0+++++0+++0')
input()