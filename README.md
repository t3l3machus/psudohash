# psudohash
[![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-red.svg)](https://github.com/t3l3machus/psudohash/blob/main/LICENSE) 
<img src="https://img.shields.io/badge/Maintained%3F-Yes-23a82c">  

## Purpose
psudohash is a password list generator for orchestrating brute force attacks. It imitates certain password creation patterns commonly used by humans, like substituting a word's letters with symbols or numbers, using char-case variations, adding a common padding before or after the word and more. It is keyword-based and highly customizable.

### Pentesting Corporate Environments
System administrators and employees tend to use the Company's name (or a subset of the name) as password for Wi-Fi access points, network devices and application or even domain accounts. With the company's name as input and the most basic options, psudohash will produce a wordlist with all possible character substitutions, char-case variations and more. Take a look at the following example:
![usage_example_png](https://raw.github.com/t3l3machus/psudohash/master/Screenshots/ms-example.png)

The script includes a basic character substitution schema. You can add/modify character substitution patterns by editing the source and following the data structure logic presented below (default):
```
transformations = [
	{'a' : '@'},
	{'b' : '8'},
	{'e' : '3'},
	{'g' : ['9', '6']},
	{'i' : ['1', '!']},
	{'o' : '0'},
	{'s' : ['$', '5']},
	{'t' : '7'}
]
```
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
