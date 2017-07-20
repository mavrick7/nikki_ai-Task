from itertools import count, product, islice
from string import ascii_uppercase

def multiletters(seq):
    for n in count(1):
        for s in product(seq, repeat=n):
            yield ''.join(s)



def cipher(m = 25, n=29):
	s = ascii_uppercase
	x = list(islice(multiletters(s),676))
	ciph = {}

	for i in range(1,677):
		ciph[i] = x[i-1]

	for a in range(m, n+1):
		print(ciph[a])	

		


def main():
	
	s = int(input("Please Enter Start b/w 1-676 : "))
	e = int(input("Please Enter End b/w 1-676 greater than Start : "))

	cipher(s,e)





if __name__ == "__main__":
	main()
	