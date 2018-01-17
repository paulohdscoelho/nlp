import sys
with open('tweetsCatalunhaCrus.txt') as entrada:
	i = 0
	for line in entrada:
		i+=1
		try:
			print(line.strip().split('\t')[2])
		except IndexError:
			print('None')


