# Just display IPA

import eng_to_ipa as ipa

debug = False

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
	
	# Remove all ' and ˌ from it, stress markings
	converted = converted.replace("ˈ", "")
	converted = converted.replace("ˌ", "")
	print(f"\nIPA: {converted}\n")