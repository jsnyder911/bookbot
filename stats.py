import sys
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():
	book_text = get_book_text(sys.argv[1])
	word_count = get_num_words(book_text)
	letters = get_book_text(sys.argv[1])
	print(f"Found {word_count} total words")


def get_num_words(book_text):
	words = book_text.split()
	num_words = len(words)
	return  num_words

def num_letters():
	char_count_dict = {}
	words = get_book_text(sys.argv[1]).split()
	for word in words:
		lower_case = word.lower()
		for letter in lower_case:
			if letter not in char_count_dict:
				char_count_dict[letter] = 1
			else:
				char_count_dict[letter] += 1
	return char_count_dict

def sort_on(items):
	return items["num"]
