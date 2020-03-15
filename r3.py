def function(filename):
	with open(filename,'r', encoding='utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip())

			s = line.split(' ')
			time = s[0][:5]
			print(time) 

def main():
	read_lines = function('viki.txt',)
main()