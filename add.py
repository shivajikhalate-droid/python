"""Simple addition utility: add two numbers.

Usage:
 - As CLI: `python add.py 2 3` prints 5
 - Interactive: run without args and follow prompts
"""

def add(a, b):
	return a + b


if __name__ == "__main__":
	import sys

	def _to_number(s):
		try:
			return float(s)
		except ValueError:
			raise

	if len(sys.argv) >= 3:
		try:
			x = _to_number(sys.argv[1])
			y = _to_number(sys.argv[2])
		except ValueError:
			print("Please provide two numeric arguments")
			sys.exit(1)
		result = add(x, y)
		# print as int when both inputs were whole numbers
		if x.is_integer() and y.is_integer():
			print(int(result))
		else:
			print(result)
	else:
		try:
			x = _to_number(input("Enter first number: "))
			y = _to_number(input("Enter second number: "))
		except ValueError:
			print("Invalid input; please enter numeric values")
			sys.exit(1)
		print(add(x, y))