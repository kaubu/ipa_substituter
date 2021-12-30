import eng_to_ipa as ipa

import json

debug = False

def sentence_capitalize(string1: str):
	sentences = string1.split(". ")
	sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
	string2 = ". ".join(sentences2)
	return string2

print("""[IPA Substituter]
1. Make a JSON file with the format 'ipa': 'substitution'
2. Load it here
3. It will output""")

ipa_dict_loc = input("Location of the JSON file: ")
ipa_dict = None

with open(ipa_dict_loc, encoding="utf8") as dict_file:
	ipa_dict = json.load(dict_file)

while True:
	# Repair the input
	ipa_input = input(">> ")
	ipa_input = ipa_input.replace("’", "'") # eng_to_ipa doesn't recognize ’s
	
	# Convert the English to IPA
	converted = ipa.convert(ipa_input)
	if debug: print(f"{converted}")
	
	# Remove all ' and ˌ from it, stress markings
	converted = converted.replace("ˈ", "")
	converted = converted.replace("ˌ", "")
	print(f"\nIPA: {converted}\n")

	# Translate using the JSON file
	for word, initial in ipa_dict.items():
		converted = converted.replace(word.lower(), initial)
	
	print(f"Converted: {converted}\n")
	print(f"Capitalized: {sentence_capitalize(converted)}\n")