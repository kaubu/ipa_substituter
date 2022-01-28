# To just substitute anything

import json

debug = False

def sentence_capitalize(string1: str):
	sentences = string1.split(". ")
	sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
	string2 = ". ".join(sentences2)
	return string2

print("""[Plain Substituter]
1. Make a JSON file with the format 'to substitute': 'substitution'
2. Load it here
3. It will output""")

sub_dict_loc = input("Location of the JSON file: ")
sub_dict = None

with open(sub_dict_loc, encoding="utf8") as dict_file:
	sub_dict = json.load(dict_file)

while True:
	# Repair the input
	plain_input = input(">> ").lower()
	plain_input = plain_input.replace("’", "'") # eng_to_ipa doesn't recognize ’s
	
	# Remove all ' and ˌ from it, stress markings
	converted = plain_input.replace("ˈ", "")
	converted = converted.replace("ˌ", "")

	# Translate using the JSON file
	for word, initial in sub_dict.items():
		converted = converted.replace(word.lower(), initial)
	
	print(f"Converted: {converted}\n")
	print(f"Capitalized: {sentence_capitalize(converted)}\n")