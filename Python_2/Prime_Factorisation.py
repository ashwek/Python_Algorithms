from sys import stdout

try:
	num = int(raw_input("\nEnter a number to find its prime factors = "))
	num = abs(num)
	flag=total=0
	stdout.write("\n -> Factors of "+str(num)+" are : ")
	while(num!=1):
		flag = 0
		for i in range(2, num):
			if(num % i == 0):
				stdout.write(str(i) + ",")
				num = num / i
				total+=1
				flag = 1
				break
		if(flag == 0):
			stdout.write(str(num))
			total+=1
			num=1

	print "\n\nThere are", total, "factors\n"
except ValueError: print"\n*** Invalid Input ***"
