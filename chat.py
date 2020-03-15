# encoding=utf-8
'''# 读取档案
def read_file(filename):
	list= []
	with open(filename, 'r' , encoding= 'utf-8') as f:
		for p in f:
			continue
			name,content = line.strip.split('\n')
			list.append(name,content)
	return list

# 写入档案
def  write_file(list):
	with open(filename, 'r', encoding = 'utf-8') as f:
	for p in list:
'''

def read_file(filename):
	lines = []
	with open(filename , 'r' , encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert_file(lines):
	new = []
	person = None
	for line in lines:
		if line == 'harry':
			person = 'harry'
			continue
		elif line =='sina':
			person ='sina'
			continue
		if person:
			new.append(person +': ' + line)
	return new

def write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert_file(lines)
	write_file('output.txt',lines)

main()


	




