import eng_to_ipa as ipa

import json

debug = False

print("""[IPA Substituter]
1. Make a JSON file with the format 'ipa': 'substitution'
2. Load it here
3. It will output""")

ipa_dict_loc = input("Location of the JSON file: ")
ipa_dict = None

with open(ipa_dict_loc, encoding="utf8") as dict_file:
	ipa_dict = json.load(dict_file)

while True:
	# Convert the English to IPA
	converted = ipa.convert(input(">> "))
	if debug: print(f"{converted}")
	
	# Remove all ' from it, stress markings
	converted = converted.replace("ˈ", "")
	print(f"IPA: {converted}")

	# Translate using the JSON file
	for word, initial in ipa_dict.items():
		converted = converted.replace(word.lower(), initial)
	
	print(f"End: {converted}")