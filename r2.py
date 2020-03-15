def read_file(filename):
	lines = []
	with open(filename , 'r' , encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert_file(lines):
	new = []
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0

	for line in lines:
		s =line.split(' ')
		time =s[0]
		name =s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count +=1
			elif s[2] =='圖片':
				allen_image_count +=1
			else:
				allen_word_count += len(s[2:])
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count +=1
			elif s[2] =='圖片':
				viki_image_count +=1
			else:                 # else 就理解为如果全都不是的话
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen 说了',allen_word_count, 'allen贴了',allen_sticker_count,'allen画了', allen_image_count)
	print('viki说了',viki_word_count, 'viki贴了',viki_sticker_count, 'viki画了', viki_image_count)

	return(lines)


	#n[:3]表示可以拿到前三个
	#n[2:4]可以拿到一个清单装n[2]

def write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('viki.txt')
	lines = convert_file(lines)
	write_file('output2.txt', lines)

main()