from sys import stdout

opt='Y'
while((opt=='y')|(opt=='Y')):
	Text=raw_input("Enter Anything below :\n=> ")
	Char_Count={}
	
	for each in Text:
		try: Char_Count[each]+=1
		except KeyError: Char_Count.update({each:1})

	print "\n\tCount : "
	for each in Char_Count.keys(): stdout.write("\t "+each+" = "+str(Char_Count[each])+"\n")

	opt=raw_input("\n\nDo you want to try again [Y/N] = ")
