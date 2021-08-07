from scanner import BasicScanner
from parser import BasicParser
from executor import BasicExecute



if __name__ == '__main__':
	scanner = BasicScanner()
	parser  = BasicParser()
	print('Mari kita cobaaaaa')
	env = {}
	
	while True:
		
		try:
			text = input('Compiler Kita > ')
		
		except EOFError:
			break
		
		if text:
			tree = parser.parse(scanner.tokenize(text))
			BasicExecute(tree, env)
