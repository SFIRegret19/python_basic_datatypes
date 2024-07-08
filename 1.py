# 1st program
print((9**0.5) * 5) # Answer: 15.0
# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1) #Answer: True
# 3rd program
print((1234 % 1000 // 10) + (5678 % 1000 // 10)) #Answer: 90
# 4th program
print((int(13.42 * 100) // 100 == int(42.13 * 100) % 100) or (int(13.42 * 100) % 100 == int(42.13 * 100) // 100)) #Answer: True
#------- or -------
a, b = int(13.42 * 100), int(42.13 * 100)
print((a // 100 == b % 100) or (a % 100 == b // 100)) #Answer: True