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

capitalizations = False
input_capitalization = input("Print captializations (y/[n])? ").lower()

if input_capitalization == "yes" or input_capitalization == "y":
	capitalizations = True

stresses = False
input_stresse = input("Print stresses (y/[n])? ").lower()

if input_stresse == "yes" or input_stresse == "y":
	stresses = True

show_ipa = True
input_show_ipa = input("Print IPA ([y]/n)? ").lower()

if input_show_ipa == "no" or input_show_ipa == "n":
	show_ipa = False

while True:
	# Repair the input
	ipa_input = input(">> ")
	if ipa_input == "" or ipa_input == None: # It will error otherwise
		print()
		continue

	ipa_input = ipa_input.replace("’", "'") # eng_to_ipa doesn't recognize ’s
	
	# Convert the English to IPA
	converted = ipa.convert(ipa_input)
	if debug: print(f"{converted}")
	
	if not stresses:
		# Remove all ' and ˌ from it, stress markings
		converted = converted.replace("ˈ", "")
		converted = converted.replace("ˌ", "")
	
	print(f"\nIPA: {converted}\n")

	# Translate using the JSON file
	for word, initial in ipa_dict.items():
		converted = converted.replace(word.lower(), initial)
	
	print(f"Converted: {converted}\n")
	if capitalizations: print(f"Capitalized: {sentence_capitalize(converted)}\n")