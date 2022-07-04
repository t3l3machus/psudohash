# psudohash
[![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-red.svg)](https://github.com/t3l3machus/psudohash/blob/main/LICENSE) 
<img src="https://img.shields.io/badge/Maintained%3F-Yes-23a82c">  

## Purpose
psudohash is a password generator that imitates certain commonly used password creation patterns that humans use, like substituting a word's characters with symbols or numbers, using char-case variations, adding a common padding before or after the word etc. It is keyword-based and highly customizable.

### Pentesting Corporate Environemnts
System administrators and employees tend to use the Company's name (or a subset of the name) as password for Wi-Fi access points, network devices and application or even domain accounts. With the company's name as input and the most basic options, psudohash will produce a wordlist with all possible character substitution and case variations and more. Take a look at the following example:
![usage_example_png](https://raw.github.com/t3l3machus/psudohash/master/Screenshots/example.png)

The script includes a basic character substitution schema. You can add/modify character substitution patterns by edditing the source and following the data structure presented below (default):
```

```
### Individuals
When it comes to people, i think we all have (more or less) set passwords using a mutation of one or more words that mean something to us, like our name or wife/kid/pet/band names, sticking the year we were born as padding at the end or maybe a supper secure padding like "!@#". Well guess what?

## Screenshot
![usage_example_png](https://raw.github.com/t3l3machus/psudohash/master/Screenshots/psudohash.png)

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

## Future 
I'm gathering information regarding commonly used password creation patterns to enhance the tool's capabilities.
