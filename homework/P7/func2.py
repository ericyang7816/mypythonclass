def changeDict(dict):
	newdict = {}
	for key in dict:
		newdict.update({}.fromkeys(dict[key],key))
	print("Current: "+str(newdict))