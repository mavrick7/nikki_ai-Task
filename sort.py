import sys

def sort_by_len(li):
	return sorted(li, key=len)
	


def input():
	li = []
	for i in sys.stdin:
		for x in i.split():
			li.append(str(x))

	return li




def main():
	li = input()
	print (sort_by_len(li ))


if __name__ == "__main__":
	main()







