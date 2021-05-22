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