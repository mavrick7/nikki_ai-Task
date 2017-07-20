def fac(n = 20000000):
	prime_fac = []
	
	d = 2
	i = int(n/2)

	while d <= i :
		if n%d == 0:
			prime_fac.append(d)

		d += 1
	print(prime_fac)	
			



def main():
	fac()
	

if __name__ == "__main__":
	main()	