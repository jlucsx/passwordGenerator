import random
import requests


def get_quote():
	"get the quotes-in-json file from freecodecamp's article suggestion then return one of them"
	url = "https://type.fit/api/quotes"
	response = requests.get(url)
	response_json = response.json()
	resp_quote = random.choice(response_json)
	resp_quote_content = resp_quote["text"]

	return resp_quote_content


def remove_duplicates(quote):
	"remove the duplicate characters inside a given quote then return the result"
	quote = quote.lower()
	
	sanitized_qt = []
	for char in set(quote):
		if char.isalpha():
			sanitized_qt.append(char)
	return sanitized_qt


def switchcase_char(uniq_chars_qt):
	"switch the case of each character of a given unique-char-quote then return the result"
	sanit_qt_switchcased = []
	for i, char in enumerate(uniq_chars_qt):
		if i % 2 == 0:
			sanit_qt_switchcased.append(char.upper())
			continue
		sanit_qt_switchcased.append(char)
	return sanit_qt_switchcased


def insert_nums_and_symbs(switchcased_qt):
	"insert numbers and symbols inside a given quote (list)"
	num = [str(n) for n in range(0, 10)]
	symb = ["@", "*", "!", "#", "&", "%", "$"]
	
	additions_inserted_qt = switchcased_qt[:9]
	for i in range(10):
		if i % 3 == 0:
			choice = random.choice(symb)
			additions_inserted_qt.insert(i+1, choice)
			symb.remove(choice)
			continue
		if i % 2 == 0:
			choice = random.choice(num)
			additions_inserted_qt.insert(i+2, choice)
			num.remove(choice)
			continue
	
	return additions_inserted_qt


def generate_password():
	"get the quote and, step-by-step, transform it in a reasonable secure password then return it"
	quote = get_quote()
	unique_chars_qt = remove_duplicates(quote)
	switched_chars_qt = switchcase_char(unique_chars_qt)
	addit_inserted_qt = insert_nums_and_symbs(switched_chars_qt)
	password = str().join(addit_inserted_qt)

	return password
	
genrtd_pass = generate_password()
print(genrtd_pass)