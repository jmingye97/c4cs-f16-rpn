#!/usr/bin/env python3

import operator
import logging

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'+=': operator.iadd,
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		logging.debug(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()
def helloWorld():
	print("Hello World!");
def main():
	logging.basicConfig(filename='out.log', filemode='w', level=logging.DEBUG)
	while True:
		result = calculate(input("rpn calc> "))
		logging.info("Result: ", result)
		print("Hello World!")

if __name__ == '__main__':
	main()
