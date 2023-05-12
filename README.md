# psudohash
[![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-red.svg)](https://github.com/t3l3machus/psudohash/blob/main/LICENSE) 
<img src="https://img.shields.io/badge/Maintained%3F-Yes-23a82c">  

## Purpose
psudohash is a password list generator for orchestrating brute force attacks. It imitates certain password creation patterns commonly used by humans, like substituting a word's letters with symbols or numbers, using char-case variations, adding a common padding before or after the word and more. It is keyword-based and highly customizable.

### Pentesting Corporate Environments
System administrators and other employees often use a mutated version of the Company's name to set passwords (e.g. Am@z0n_2022). This is commonly the case for network devices (Wi-Fi access points, switches, routers, etc), application or even domain accounts. With the most basic options, psudohash can generate a wordlist with all possible mutations of one or multiple keywords, based on common character substitution patterns (customizable), case variations, strings commonly used as padding and more. Take a look at the following example:  

![usage_example_png](https://raw.github.com/t3l3machus/psudohash/master/Screenshots/ms-example.png)

The script implements the following character substitution schema. You can add/modify character substitution mappings by editing the `transformations` list in `psudohash.py` and following the data structure presented below (default):
```
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
```  

When appending a year value to a mutated keyword, psudohash will do so by utilizing various seperators. by default, it will use the following seperators which you can modify by editing the `year_seperators` list:  
```
year_seperators = ['', '_', '-', '@']
```
For example, if the given keyword is "amazon" and option `-y 2023` was used, the output will include "amazon2023", "amazon_2023", "amazon-2023", "amazon@2023", "amazon23", "amazon_23", "amazon-23", "amazon@23".
  
### Individuals
When it comes to people, i think we all have (more or less) set passwords using a mutation of one or more words that mean something to us e.g., our name or wife/kid/pet/band names, sticking the year we were born at the end or maybe a super secure padding like "!@#". Well, guess what?

![usage_example_png](https://raw.github.com/t3l3machus/psudohash/master/Screenshots/multiple-words.png)

## Installation
No special requirements. Just clone the repo and make the script executable:
```
git clone https://github.com/t3l3machus/psudohash
cd ./psudohash
chmod +x psudohash.py
```  
## Usage
```
./psudohash.py [-h] -w WORDS [-an LEVEL] [-nl LIMIT] [-y YEARS] [-ap VALUES] [-cpb] [-cpa] [-cpo] [-o FILENAME] [-q]
```
The help dialog [ -h, --help ] includes usage details and examples.
## Usage Tips
1. Combining options `--years` and `--append-numbering` with a `--numbering-limit` ≥ last two digits of any year input, will most likely produce duplicate words because of the mutation patterns implemented by the tool. 
2. If you add custom padding values and/or modify the predefined common padding values in the source code, in combination with multiple optional parameters, there is a small chance of duplicate words occurring. psudohash includes word filtering controls but for speed's sake, those are limited.

## Future 
I'm gathering information regarding commonly used password creation patterns to enhance the tool's capabilities.
