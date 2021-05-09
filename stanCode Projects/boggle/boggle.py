"""
File: boggle.py
Name: Amy Su
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = []  # 開list存字典
letters = []  # 開list存使用者輸入
used_position=[]
number = 0  # 記錄找到幾個字


def main():
	"""
	TODO:
	"""
	read_dictionary()  # 讀字典
	lst1 = (input('1 row of letters: ').split())
	lst2= (input('2 row of letters: ').split())
	lst3 = (input('3 row of letters: ').split())
	lst4 = (input('4 row of letters: ').split())

	letters.append(lst1)
	letters.append(lst2)
	letters.append(lst3)
	letters.append(lst4)
	print(letters)

	play_boggle()
	print(f'There are {number} words in total.')  # 印出找到的成果

# [[f, y, c, l], [i, o, m, g]
def play_boggle(): # 選第一個字，再不停的recursion接下去
	global used_position
	for i in range(4): 	# 選第一個字
		for j in range(4):
			used_position =[]  # 要把使用過的list清空
			word = ''  # 開始把找到的字裝箱
			word += letters[i][j]  # 串上第一個字
			used_position.append((i, j))  # 位置要記錄起來
			helper(word, [i, j], [i, j])


def helper(word, old_position,now_position):
	"""
	:param word: 紀錄現在串了什麼英文字
	:param old_position: 紀錄上一層recursion的位置
	:param now_position: 紀錄這一層recursion的位置
	"""
	global letters, number, used_position
	old_position = now_position  # 更新位子
	if has_prefix(word):  # if True, 執行以下code
		if word in dictionary and len(word) >= 4:  # Base case
			print('Found' + '"' + str(word) + '"')
			number += 1  # 記錄找到的字
			dictionary.remove(word)  # 把字從字典remove，不然會一直迴圈
			helper(word, old_position,now_position)
		else:
			for i in range(-1, 2, 1):  # 跑-1,0,1
				for j in range(-1, 2, 1):
					x = old_position[0] + i  # 原本x位置左右跑
					y = old_position[1] + j  # 原本y位置上下跑
					if 0 <= x < 4 and 0 <= y < 4:  # 在boggle的範圍裡面
						if (x, y) not in used_position:  # 要選沒有被放過的
							used_position.append((x, y))  # 位置要記錄起來
							# choose
							word += letters[x][y]
							now_position = [x, y]  # 存新位子
							# explore
							helper(word, old_position, now_position)
							# un-choose
							used_position.pop()  # pop掉才有辦法被重串
							word = word[:len(word)-1]

			# 找出其他八個字
			# 右邊: letters[y][x + 1]
			# 左邊: letters[y][x - 1]
			# 上面: letters[y - 1][x]
			# 下面: letters[y + 1][x]
			# 右上: letters[y - 1][x + 1]
			# 左上: letters[y - 1][x - 1]
			# 右下: letters[y + 1][x + 1]
			# 左下: letters[y + 1][x - 1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for char in dictionary:  # char 為dictionary裡的單字
		if char .startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
