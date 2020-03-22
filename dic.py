# dictionary 提取文字的个数

def average_count(filename):
	data = []
	count = 0
	with open(filename,'r') as f:
		for line in f:
			data.append(line)
			count += 1
		if count % 1000 == 0:
			print(len(data))

		print('档案共有，总共有',len(data),'笔资料' )
		newlen = []
		for d in data:
			if len(d) < 100:
				newlen.append(d)
		print('一共有',len(newlen),'笔留言小于100')
		#print(newlen[])

def extract(filename):
	with open(filename,'r',encoding = 'utf-8-sig') as d:
		wc = {}
		for line in d:
			words = line.split(' ')
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1

		for word in wc:
			if wc[word] > 100:
				print(word,wc[word])
		print('字数', len(wc))

		while True:
			word = input('请问你想要什么字：')
			if word =='q':
				print('感谢使用')
				break
			elif word in wc:
				print(word, '出现过的次数为', wc[word])
			else:
				print('感谢使用,没有这个词')

def main():

	average_count('reviews.txt',)
	words = extract('reviews.txt')

main()