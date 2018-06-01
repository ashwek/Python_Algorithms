try:
	num = float(raw_input("\n\tEnter a number = "))
	try:
		limit = int(raw_input("\tEnter a limit = "))
		N_width = len(str(limit))
		R_width = len(str(num*limit))
		for n in range (1, limit+1):
			print "\t ->", num, "*", str(n).center(N_width), "=", str(num*n).center(R_width)

	except ValueError: print "\n\t*** Invalid Limit Entered ***\n"
except ValueError: print "\n\t*** Invalid Number Entered ***\n"
