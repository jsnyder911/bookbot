import sys
from stats import get_book_text
from stats import main
from stats import get_num_words
from stats import num_letters
from stats import sort_on

if len(sys.argv) != 2:
	print ("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

words = num_letters()
main()
list = []

for key in words:
  values = words[key]
  list.append({"char" : key, "num" : values})

list.sort(reverse=True, key=sort_on)

for line in list:
	print(f'{line["char"]}: {line["num"]}')
