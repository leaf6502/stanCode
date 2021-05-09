"""
File: largest_digit.py
Name: Amy Su
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	return int(find_largest_digit_helper(n, 0))


def find_largest_digit_helper(n, max):
	# base case
	if n == 0:
		return max
	else:
		# 先判斷數字是否為正數還是負數，如果是負的一律轉成正的
		if n < 0:
			n = -n
		# 數字對10取餘數，然後跟ｍａｘ比較
		num = n % 10
		if num > max:
			max = num
		# 數字扣掉餘數，再除以10，使用recursion繼續往下找
		return find_largest_digit_helper((n-num) // 10, max)




	# 	if 0 < n // 10 < 1:
	# 	print(n)
	# else:
	# 	# 怎麼知道是幾位數
	# 	if k is int and k < n // 10 < k + 1:
	# 		a = abs(n) // 10 ** k
	# 		b = abs(n) // 10 ** (k - 1)
	# 		if a <= b:  # 1 <= 2
	# 			return n - (a * 10 ** k)  # 12345 -->2345
	# 		else:
	# 			return n - (a * 10 ** k) - (b * 10 ** (k - 1)) + (a * 10 ** (k - 1)) # 21345 -->2345





if __name__ == '__main__':
	main()
