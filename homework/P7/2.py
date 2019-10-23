dicta={2:'b',1:'a',3:'c'}
print("Previous: "+str(dicta))  
def changedict(dict):
	newdict = {}
	for key in dict:
		newdict.update({}.fromkeys(dict[key],key))
	print("Current: "+str(newdict))
changedict(dicta)