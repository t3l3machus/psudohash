#!/bin/python3
#
# Created by Panagiotis Chartas (t3l3machus)
# https://github.com/t3l3machus


import argparse, sys, itertools

# -------------- Arguments & Usage -------------- #
parser = argparse.ArgumentParser()

parser.add_argument("-w", "--word", action="store", help = "Main word to transform", required = True)
parser.add_argument("-sn", "--serial-numbering", action="store", help = "Add comma seperated values to common paddings (must be used with -cp OR -cpb OR -cpa)")
parser.add_argument("-y", "--years", action="store", help = "Comma seperated OR range of year values (e.g., 1990,2022 OR 1990-2000)")
parser.add_argument("-ap", "--append-padding", action="store", help = "Add comma seperated values to common paddings (must be used with -cp OR -cpb OR -cpa)")
parser.add_argument("-cpb", "--common-paddings-before", action="store_true", help = "Add common paddings before each mutated word") 
parser.add_argument("-cpa", "--common-paddings-after", action="store_true", help = "Add common paddings after each mutated word") 
parser.add_argument("-cpo", "--custom-paddings-only", action="store_true", help = "Use only user provided paddings for word mutations (must be used with -ap AND (-cp OR -cpb OR -cpa))") 
parser.add_argument("-o", "--output", action="store", help = "Output filename")
parser.add_argument("-q", "--quiet", action="store_true", help = "Do not print the banner on startup")

args = parser.parse_args()

# Add user appended padding strings
if args.append_padding:
	for item in args.append_padding.split(','):
		if item != '': common_paddings.append(item)
			

# Create years list
def bad_years_input():
	parser.print_usage()
	print('\nIllegal year(s) input. Acceptable years range: 1000 - 3200.\n')
	sys.exit(1)					


if args.years:
	years = []
	
	if args.years.count(',') == 0 and args.years.count('-') == 0 and args.years.isdecimal() and int(args.years) >= 1000 and int(args.years) <= 3200:
		years.append(str(args.years))

	elif args.years.count(',') > 0:
		for year in args.years.split(','):
			if year.strip() != '' and year.isdecimal() and int(year) >= 1000 and int(year) <= 3200: 
				years.append(year)
			else:
				bad_years_input()

	elif args.years.count('-') == 1:
		years_range = args.years.split('-')
		start_year = years_range[0]
		end_year = years_range[1]
		
		if (start_year.isdecimal() and int(start_year) < int(end_year) and int(start_year) >= 1000) and (end_year.isdecimal() and int(end_year) <= 3200):
			for y in range(int(years_range[0]), int(years_range[1])+1):
				years.append(str(y))
		else:
			bad_years_input()
	else:
		bad_years_input()
			

# Colors
LOGO = '\033[38;5;40m'
LOGO2 = '\033[38;5;41m'
GREEN = '\033[38;5;82m'
ORANGE = '\033[0;38;5;214m'
RED = '\033[1;31m'
END = '\033[0m'
BOLD = '\033[1m'

def banner():

	pad = '   '
	print('\n')
	print(f'{pad}{LOGO}█▀▄ ▄▀▀ █ █ █▀▄ ▄▀▄ █▄█ ▄▀▄ ▄▀▀ █▄█')
	print(f'{pad}{LOGO2}█▀  ▄██ ▀▄█ █▄▀ ▀▄▀ █ █ █▀█ ▄██ █ █{END}')
	print('\t         Created by t3l3machus\n')


# ----------------( Base Settings )---------------- #
mutations_cage = []
mutations_final = []
outfile = args.output if args.output else 'output.txt'
trans_keys = []

transformations = [
	{'a' : '@'},
	{'e' : '3'},
	{'g' : ['9', '6']},
	{'i' : ['1', '!']},
	{'o' : '0'},
	{'s' : ['$', '5']},
	{'t' : '7'}
]

for t in transformations:
	for key in t.keys():
		trans_keys.append(key)

# Paddings
if (args.common_paddings_before or args.common_paddings_after) and not args.custom_paddings_only:

	common_paddings = [
		'12', '23', '34', '45', '56', '67', '78', '89', '90'\
		'123', '234', '345', '456', '567', '678', '789', '890',\
		'.', '!', ';', '?', '!@', '@#', '#$', '$%', '%^', '^&', '&*', '*(', '()', \
		'!@#', '@#$', '#$%', '$%^', '%^&', '^&*', '&*(', '*()', ')_+',\
		'1!1', '!@!', '@#@', '$$$', '!@#$%', '123!@#', '12345'
		#'!!!', '@@@', '###', '$$$', '%%%', '^^^', '&&&', '***', '(((', ')))', '---', '+++'
	]

elif (args.common_paddings_before or args.common_paddings_after) and (args.custom_paddings_only and args.append_padding):
	common_paddings = []

elif not (args.common_paddings_before or args.common_paddings_after):
	pass

else:
	parser.print_usage()
	print('\nIllegal padding settings.\n')
	sys.exit(1)			

if args.append_padding:
	for val in args.append_padding.split(','):
		if val.strip() != '' and val not in common_paddings: 
			common_paddings.append(val)
		

# ----------------( Functions )---------------- #
def evalTransformations(w):
	
	trans_chars = []
	total = 1
	c = 0
	
	w = list(w)
	for char in w:
		for t in transformations:
			if char in t.keys():
				trans_chars.append(c)
				if isinstance(t[char], list):
					total *= 3
				else:
					total *= 2
		c += 1
			
	return [trans_chars, total]

		
						
def mutate(tc):
	
	global trans_keys, mutations_cage, mutations_final
	
	i = trans_keys.index(args.word[tc].lower())
	trans = transformations[i][args.word[tc].lower()]
	limit = len(trans) * len(mutations_cage)
	c = 0
	
	for m in mutations_cage:
		w = list(m)			

		if isinstance(trans, list):
			for tt in trans:
				w[tc] = tt
				transformed = ''.join(w)
				mutations_cage.append(transformed)
				c += 1
		else:
			w[tc] = trans
			transformed = ''.join(w)
			mutations_cage.append(transformed)
			c += 1
		
		if limit == c: break
		
	return mutations_cage
	


def mutations_handler(trans_chars, total):
	
	global mutations_cage, mutations_final
	
	container = []
	
	for word in mutations_final:
		mutations_cage = [word.strip()]	
		for tc in trans_chars:
			results = mutate(tc)
		container.append(results)
	
	for m_set in container:
		for m in m_set:
			mutations_final.append(m)
	
	mutations_final = unique(mutations_final)

	with open(outfile, 'w') as wordlist:		
		for m in mutations_final:
			wordlist.write(m + '\n')



def grab_wordlist():
	
	wordlist = open(outfile, 'r')
	words = wordlist.readlines()
	wordlist.close()
	return words



def mutateCase(word):
	trans = list(map(''.join, itertools.product(*zip(word.upper(), word.lower()))))
	return trans



def caseMutationsHandler(word):
	
	case_mutations = mutateCase(word)

	for m in case_mutations:
		mutations_final.append(m)



def unique(l):
  
	unique_list = []

	for i in l:
		if i not in unique_list:
			unique_list.append(i)
    
	return unique_list	



def mutate_years():
	
	current_mutations = mutations_final.copy()
	
	with open(outfile, 'a') as wordlist:
		for word in current_mutations:
			for y in years:				
				wordlist.write(f'{word}{y}\n')
				wordlist.write(f'{word}_{y}\n')
				wordlist.write(f'{word}{y[2:]}\n')
				mutations_final.append(f'{word}{y}')
				mutations_final.append(f'{word}_{y}')
				mutations_final.append(f'{word}{y[2:]}')		



def append_paddings_before():

	current_mutations = mutations_final.copy()
	wfilter = []
	
	with open(outfile, 'a') as wordlist:
		for word in current_mutations:
			for val in common_paddings:
				if f'{val}{word}' not in wfilter:
					wordlist.write(f'{val}{word}\n')
					wfilter.append(f'{val}{word}')
					
				if f'{val}_{word}' not in wfilter:
					wordlist.write(f'{val}_{word}\n')
					wfilter.append(f'{val}_{word}')	



def append_paddings_after():

	current_mutations = mutations_final.copy()
	wfilter = []
	
	with open(outfile, 'a') as wordlist:
		for word in current_mutations:
			for val in common_paddings:	
				if f'{word}{val}' not in wfilter:			
					wordlist.write(f'{word}{val}\n')
					wfilter.append(f'{word}{val}')
				
				if f'{word}_{val}' not in wfilter:	
					wordlist.write(f'{word}_{val}\n')
					wfilter.append(f'{word}_{val}')



def calculate_output():
	
	global trans_keys
	
	c = 0
	total = 1
	basic_total = 1
	basic_size = 0
	size = 0
	
	# Basic mutations calc
	for char in args.word:
		if char in trans_keys:
			i = trans_keys.index(args.word[c].lower())
			trans = transformations[i][args.word[c].lower()]
			basic_total *= (len(trans) + 2)		
		else:
			basic_total *= 2
			
		c += 1
	
	total = basic_total 
	basic_size = total * (len(args.word) + 1)
	size = basic_size
	
	# Adding years mutations calc
	if args.years:
		patterns = 3
		year_chars = 4
		_year = 5
		year_short = 2
		yrs = len(years)
		size += (basic_size * patterns * yrs) + (basic_total * year_chars * yrs) + (basic_total * _year * yrs) + (basic_total * year_short * yrs)
		total += total * len(years) * 3
		basic_total = total
		basic_size = size
	
	# Common paddings mutations calc
	patterns = 2
	
	if args.common_paddings_after or args.common_paddings_before:
		paddings_len = len(common_paddings)
		pads_wlen_sum = sum([basic_total*len(w) for w in common_paddings])
		_pads_wlen_sum = sum([basic_total*(len(w)+1) for w in common_paddings])
		
		if args.common_paddings_after and args.common_paddings_before:		
			size += ((basic_size * patterns * paddings_len) + pads_wlen_sum + _pads_wlen_sum) * 2
			total += (total * len(common_paddings) * 2) * 2
		
		elif args.common_paddings_after or args.common_paddings_before:
			size += (basic_size * patterns * paddings_len) + pads_wlen_sum + _pads_wlen_sum
			total += total * len(common_paddings) * 2

	return [total, size]



def chill():
	pass



def main():
	
	banner() if not args.quiet else chill()
	
	# Calculate output size
	total_size = calculate_output()
	concent = input(f'[{ORANGE}Warning{END}] This operation will produce a total of {BOLD}{total_size[0]}{END} words, {BOLD}{total_size[1]}{END} bytes (if no duplicates occur). Are you sure you want to proceed? [y/n]: ')
	
	if concent.lower() not in ['y', 'yes']:
		sys.exit(f'\n[{RED}X{END}] Aborting.')
		
	else:
		# Produce case mutations
		print(f'[{GREEN}*{END}] Producing character case-based transformations... ')		
		caseMutationsHandler(args.word)	
		
		# Produce char substitution mutations
		print(f'[{GREEN}*{END}] Mutating word based on commonly used character-symbol substitutions... ')
		trans = evalTransformations(args.word)	
		mutations_handler(trans[0], trans[1])
		
		# Handle years
		if args.years:
			print(f'[{GREEN}*{END}] Appending transformations based on given year(s) values... ')
			mutate_years()
		
		# Append common paddings		
		if args.common_paddings_after:
			print(f'[{GREEN}*{END}] Appending common paddings after each word mutation... ')
			append_paddings_after()
			
		if args.common_paddings_before:
			print(f'[{GREEN}*{END}] Appending common paddings before each word mutation... ')
			append_paddings_before()
		
		print(f'[{GREEN}*{END}] Completed! List saved in {outfile}')


if __name__ == '__main__':
	main()
