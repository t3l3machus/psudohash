#!/bin/python3
#
# Author: Panagiotis Chartas (t3l3machus)
# https://github.com/t3l3machus

import argparse, sys, itertools

# Colors
MAIN = '\033[38;5;50m'
LOGO = '\033[38;5;41m'
LOGO2 = '\033[38;5;42m'
GREEN = '\033[38;5;82m'
ORANGE = '\033[0;38;5;214m'
PRPL = '\033[0;38;5;26m'
PRPL2 = '\033[0;38;5;25m'
RED = '\033[1;31m'
END = '\033[0m'
BOLD = '\033[1m'

# -------------- Arguments & Usage -------------- #
parser = argparse.ArgumentParser(
	formatter_class=argparse.RawTextHelpFormatter,
	epilog='''
Usage examples:

  Basic:
      python3 psudohash.py -w <keywords> -cpa
	
  Thorough:
      python3 psudohash.py -w <keywords> -cpa -an 3 -y 1990-2022
'''
	)

parser.add_argument("-w", "--words", action="store", help = "Comma seperated keywords to mutate", required = True)
parser.add_argument("-an", "--append-numbering", action="store", help = "Append numbering range at the end of each word mutation (before appending year or common paddings).\nThe LEVEL value represents the minimum number of digits. LEVEL must be >= 1. \nSet to 1 will append range: 1,2,3..100\nSet to 2 will append range: 01,02,03..100 + previous\nSet to 3 will append range: 001,002,003..100 + previous.\n\n", type = int, metavar='LEVEL')
parser.add_argument("-nl", "--numbering-limit", action="store", help = "Change max numbering limit value of option -an. Default is 50. Must be used with -an.", type = int, metavar='LIMIT')
parser.add_argument("-y", "--years", action="store", help = "Singe OR comma seperated OR range of years to be appended to each word mutation (Example: 2022 OR 1990,2017,2022 OR 1990-2000)")
parser.add_argument("-ap", "--append-padding", action="store", help = "Add comma seperated values to common paddings (must be used with -cpb OR -cpa)", metavar='VALUES')
parser.add_argument("-cpb", "--common-paddings-before", action="store_true", help = "Append common paddings before each mutated word") 
parser.add_argument("-cpa", "--common-paddings-after", action="store_true", help = "Append common paddings after each mutated word") 
parser.add_argument("-cpo", "--custom-paddings-only", action="store_true", help = "Use only user provided paddings for word mutations (must be used with -ap AND (-cpb OR -cpa))") 
parser.add_argument("-o", "--output", action="store", help = "Output filename (default: output.txt)", metavar='FILENAME')
parser.add_argument("-q", "--quiet", action="store_true", help = "Do not print the banner on startup")

args = parser.parse_args()

def exit_with_msg(msg):
	parser.print_help()
	print(f'\n[{RED}Debug{END}] {msg}\n')
	sys.exit(1)	



def unique(l):
  
	unique_list = []

	for i in l:
		if i not in unique_list:
			unique_list.append(i)
    
	return unique_list


# Append numbering
if args.numbering_limit and not args.append_numbering:
	exit_with_msg('Option -nl must be used with -an.')

if args.append_numbering:
	if args.append_numbering <= 0:
		exit_with_msg('Numbering level must be > 0.')

_max = args.numbering_limit + 1 if args.numbering_limit and isinstance(args.numbering_limit, int) else 51


# Create years list		
if args.years:
	
	years = []
	
	if args.years.count(',') == 0 and args.years.count('-') == 0 and args.years.isdecimal() and int(args.years) >= 1000 and int(args.years) <= 3200:
		years.append(str(args.years))

	elif args.years.count(',') > 0:
		for year in args.years.split(','):
			if year.strip() != '' and year.isdecimal() and int(year) >= 1000 and int(year) <= 3200: 
				years.append(year)
			else:
				exit_with_msg('Illegal year(s) input. Acceptable years range: 1000 - 3200.')

	elif args.years.count('-') == 1:
		years_range = args.years.split('-')
		start_year = years_range[0]
		end_year = years_range[1]
		
		if (start_year.isdecimal() and int(start_year) < int(end_year) and int(start_year) >= 1000) and (end_year.isdecimal() and int(end_year) <= 3200):
			for y in range(int(years_range[0]), int(years_range[1])+1):
				years.append(str(y))
		else:
			exit_with_msg('Illegal year(s) input. Acceptable years range: 1000 - 3200.')
	else:
		exit_with_msg('Illegal year(s) input. Acceptable years range: 1000 - 3200.')
			

def banner():
	padding = '  '

	P = [[' ', '┌', '─', '┐'], [' ', '├','─','┘'], [' ', '┴',' ',' ']]
	S = [[' ', '┌','─','┐'], [' ', '└','─','┐'], [' ', '└','─','┘']]
	U = [[' ', '┬',' ','┬'], [' ', '│',' ','│'], [' ', '└','─','┘']]
	D = [[' ', '┌','┬','┐'], [' ', ' ','│','│'], [' ', '─','┴','┘']]
	O =	[[' ', '┌','─','┐'], [' ', '│',' ','│'], [' ', '└','─','┘']]
	H = [[' ', '┐', ' ', '┌'], [' ', '├','╫','┤'], [' ', '┘',' ','└']]	
	A = [[' ', '┌','─','┐'], [' ', '├','─','┤'], [' ', '┴',' ','┴']]
	S = [[' ', '┌','─','┐'], [' ', '└','─','┐'], [' ', '└','─','┘']]
	H = [[' ', '┬',' ','┬'], [' ', '├','─','┤'], [' ', '┴',' ','┴']]

	banner = [P,S,U,D,O,H,A,S,H]
	final = []
	print('\r')
	init_color = 37
	txt_color = init_color
	cl = 0

	for charset in range(0, 3):
		for pos in range(0, len(banner)):
			for i in range(0, len(banner[pos][charset])):
				clr = f'\033[38;5;{txt_color}m'
				char = f'{clr}{banner[pos][charset][i]}'
				final.append(char)
				cl += 1
				txt_color = txt_color + 36 if cl <= 3 else txt_color

			cl = 0

			txt_color = init_color
		init_color += 31

		if charset < 2: final.append('\n   ')

	print(f"   {''.join(final)}")
	print(f'{END}{padding}                        by t3l3machus\n')


# ----------------( Base Settings )---------------- #
mutations_cage = []
basic_mutations = []
outfile = args.output if args.output else 'output.txt'
trans_keys = []

transformations = [
	{'a' : ['@', '4']},
	{'b' : '8'},
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

# Common Padding Values
if (args.custom_paddings_only or args.append_padding) and not (args.common_paddings_before or args.common_paddings_after):
	exit_with_msg('Options -ap and -cpo must be used with -cpa or -cpb.')
	
	
elif (args.common_paddings_before or args.common_paddings_after) and not args.custom_paddings_only:
	
	try:
		f = open('common_padding_values.txt', 'r')
		content = f.readlines()
		common_paddings = [val.strip() for val in content]
		f.close()

	except:
		exit_with_msg('File "common_padding_values.txt" not found.')

elif (args.common_paddings_before or args.common_paddings_after) and (args.custom_paddings_only and args.append_padding):
	common_paddings = []

elif not (args.common_paddings_before or args.common_paddings_after):
	common_paddings = []

else:
	exit_with_msg('\nIllegal padding settings.\n')		

if args.append_padding:
	for val in args.append_padding.split(','):
		if val.strip() != '' and val not in common_paddings: 
			common_paddings.append(val)


if (args.common_paddings_before or args.common_paddings_after):
	common_paddings = list(set(common_paddings))


# ----------------( Functions )---------------- #
# The following list is used to create variations of password values and appended years.
# For example, a passwd value {passwd} will be mutated to "{passwd}{seperator}{year}"
# for each of the symbols included in the list below.
year_seperators = ['', '_', '-', '@']



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

		

def mutate(tc, word):
	
	global trans_keys, mutations_cage, basic_mutations
	
	i = trans_keys.index(word[tc].lower())
	trans = transformations[i][word[tc].lower()]
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
	


def mutations_handler(kword, trans_chars, total):
	
	global mutations_cage, basic_mutations
	
	container = []
	
	for word in basic_mutations:
		mutations_cage = [word.strip()]	
		for tc in trans_chars:
			results = mutate(tc, kword)
		container.append(results)
	
	for m_set in container:
		for m in m_set:
			basic_mutations.append(m)
	
	basic_mutations = list(set(basic_mutations))

	with open(outfile, 'a') as wordlist:		
		for m in basic_mutations:
			wordlist.write(m + '\n')



def mutateCase(word):
	trans = list(map(''.join, itertools.product(*zip(word.upper(), word.lower()))))
	return trans



def caseMutationsHandler(word, mutability):
	
	global basic_mutations
	case_mutations = mutateCase(word)

	for m in case_mutations:
		basic_mutations.append(m)

	if not mutability:
		
		basic_mutations = list(set(basic_mutations))
		
		with open(outfile, 'a') as wordlist:		
			for m in basic_mutations:
				wordlist.write(m + '\n')



def append_numbering():
	
	global _max
	first_cycle = True
	previous_list = []
	lvl = args.append_numbering
	
	with open(outfile, 'a') as wordlist:
		for word in basic_mutations:
			for i in range(1, lvl+1):		
				for k in range(1, _max):
					if first_cycle:
						wordlist.write(f'{word}{str(k).zfill(i)}\n')
						wordlist.write(f'{word}_{str(k).zfill(i)}\n')
						previous_list.append(f'{word}{str(k).zfill(i)}')
						
					else:
						if previous_list[k - 1] != f'{word}{str(k).zfill(i)}':
							wordlist.write(f'{word}{str(k).zfill(i)}\n')
							wordlist.write(f'{word}_{str(k).zfill(i)}\n')
							previous_list[k - 1] = f'{word}{str(k).zfill(i)}'

				first_cycle = False
	del previous_list
	


def mutate_years():
	
	current_mutations = basic_mutations.copy()
	
	with open(outfile, 'a') as wordlist:
		for word in current_mutations:
			for y in years:
				for sep in year_seperators:		
					wordlist.write(f'{word}{sep}{y}\n')				
					basic_mutations.append(f'{word}{sep}{y}')
					wordlist.write(f'{word}{sep}{y[2:]}\n')
					basic_mutations.append(f'{word}{sep}{y[2:]}')		
	
	del current_mutations



def check_underscore(word, pos):
	if word[pos] == '_':
		return True
	else:
		return False
		

def append_paddings_before():

	current_mutations = basic_mutations.copy()
	
	with open(outfile, 'a') as wordlist:
		for word in current_mutations:
			for val in common_paddings:
				wordlist.write(f'{val}{word}\n')
				if not check_underscore(val, -1):
					wordlist.write(f'{val}_{word}\n')
				
					
	del current_mutations



def append_paddings_after():

	current_mutations = basic_mutations.copy()
	
	with open(outfile, 'a') as wordlist:
		for word in current_mutations:
			for val in common_paddings:	
				wordlist.write(f'{word}{val}\n')			
				if not check_underscore(val, 0):
					wordlist.write(f'{word}_{val}\n')
						
	del current_mutations



def calculate_output(keyw):
	
	global trans_keys
	
	c = 0
	total = 1
	basic_total = 1
	basic_size = 0
	size = 0
	numbering_count = 0
	numbering_size = 0
	
	# Basic mutations calc
	for char in keyw:
		if char in trans_keys:
			i = trans_keys.index(keyw[c].lower())
			trans = transformations[i][keyw[c].lower()]
			basic_total *= (len(trans) + 2)		
		else:
			basic_total = basic_total * 2 if char.isalpha() else basic_total
			
		c += 1
	
	total = basic_total 
	basic_size = total * (len(keyw) + 1)
	size = basic_size
	
	# Words numbering mutations calc
	if args.append_numbering:
		global _max
		word_len = len(keyw) + 1
		first_cycle = True
		previous_list = []
		lvl = args.append_numbering
			
		for w in range(0, total):
			for i in range(1, lvl+1):		
				for k in range(1, _max):
					n = str(k).zfill(i)
					if first_cycle:					
						numbering_count += 2						
						numbering_size += (word_len * 2) + (len(n) * 2) + 1
						previous_list.append(f'{w}{n}')
						
					else:
						if previous_list[k - 1] != f'{w}{n}':
							numbering_size += (word_len * 2) + (len(n) * 2) + 1
							numbering_count += 2
							previous_list[k - 1] = f'{w}{n}'

				first_cycle = False

		del previous_list
		
	# Adding years mutations calc
	if args.years:
		patterns = len(year_seperators) * 2
		year_chars = 4
		year_short = 2
		years_len = len(years)
		size += (basic_size * patterns * years_len)

		for sep in year_seperators:
			size += (basic_total * (year_chars + len(sep)) * years_len)
			size += (basic_total * (year_short  + len(sep)) * years_len)

		total += total * len(years) * patterns
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
	
	return [total + numbering_count, size + numbering_size]



def check_mutability(word):
	
	global trans_keys
	m = 0
	
	for char in word:
		if char in trans_keys:
			m += 1
	
	return m



def chill():
	pass



def main():
	
	banner() if not args.quiet else chill()
	
	global basic_mutations, mutations_cage
	keywords = []
	
	for w in args.words.split(','):
		if w.strip().isdecimal():
			exit_with_msg('Unable to mutate digit-only keywords.')
			
		elif w.strip() not in [None, '']:
			keywords.append(w.strip())
	
	# Calculate total words and size of output
	total_size = [0, 0]
	
	for keyw in keywords:
		count_size = calculate_output(keyw.strip().lower())
		total_size[0] += count_size[0]
		total_size[1] += count_size[1]
	
	size = round(((total_size[1]/1000)/1000), 1) if total_size[1] > 100000 else total_size[1]
	prefix = 'bytes' if total_size[1] <= 100000 else 'MB'
	fsize = f'{size} {prefix}'
	
	print(f'[{MAIN}Info{END}] Calculating output length and size...')

	# Inform user about the output size
	try:
		concent = input(f'[{ORANGE}Warning{END}] This operation will produce {BOLD}{total_size[0]}{END} words, {BOLD}{fsize}{END}. Are you sure you want to proceed? [y/n]: ')
	except KeyboardInterrupt:
		exit('\n')
	
	if concent.lower() not in ['y', 'yes']:
		sys.exit(f'\n[{RED}X{END}] Aborting.')
		
	else:
		
		open(outfile, "w").close()
		
		for word in keywords:
			print(f'[{GREEN}*{END}] Mutating keyword: {GREEN}{word}{END} ')	
			mutability = check_mutability(word.lower())
					
			# Produce case mutations
			print(f' ├─ Producing character case-based transformations... ')
			caseMutationsHandler(word.lower(), mutability)	
			
			if mutability:
				# Produce char substitution mutations
				print(f' ├─ Mutating word based on commonly used char-to-symbol and char-to-number substitutions... ')
				trans = evalTransformations(word.lower())
				mutations_handler(word, trans[0], trans[1])
				
			else:
				print(f' ├─ {ORANGE}No character substitution instructions match this word.{END}')

			# Append numbering
			if args.append_numbering:
				print(f' ├─ Appending numbering to each word mutation... ')
				append_numbering()
			
			# Handle years
			if args.years:
				print(f' ├─ Appending year patterns after each word mutation... ')
				mutate_years()
			
			# Append common paddings		
			if args.common_paddings_after or args.custom_paddings_only:
				print(f' ├─ Appending common paddings after each word mutation... ')
				append_paddings_after()
				
			if args.common_paddings_before:
				print(f' ├─ Appending common paddings before each word mutation... ')
				append_paddings_before()
			
			basic_mutations = []
			mutations_cage = []
			print(f' └─ Done!')
		
		print(f'\n[{MAIN}Info{END}] Completed! List saved in {outfile}\n')
			

if __name__ == '__main__':
	main()
