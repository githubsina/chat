# dictionary 提取文字的个数
import time
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

	sum_len = 0
	for d in data:
		sum_len = sum_len +len(d)
	print('The average length of reviews is ',sum_len/len(data))

	#快写法
	good = []
	for d in data:
		if 'good' in d:
			good.append(d)
	print('一共有',len(good),'笔留言提到good')
	print('-------------------------------------------------------')
	print('data 内含内容')
	return data


		#print(newlen[])
# 文字的计数以及查询
def extract(filename,data):
	with open(filename,'r',encoding = 'utf-8-sig') as f:
		start_time = time.time()
		wc = {}
		for d in data:
			words = d.split(' ')
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1

		for word in wc:
			if wc[word] > 100:
				print(word,wc[word])
		print('字数', len(wc))
		end_time = time.time()
		print('花了',end_time - start_time,'seconds')

		while True:
			word = input('请问你想要什么字：')
			if word =='q':
				print('感谢使用')
				break
			elif word in wc:
				print(word, '出现过的次数为', wc[word])
			else:
				print('感谢使用,没有这个词')
		print(wc)

def main():

	data = average_count('reviews.txt')
	words = extract('reviews.txt', data)

main()