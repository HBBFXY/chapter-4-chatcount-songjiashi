s = input()
eng = sum(1 for c in s if c.isalpha())
num = sum(1 for c in s if c.isdigit())
space = sum(1 for c in s if c.isspace())
other = len(s) - eng - num - space

print("英文字符: {}".format(eng))
print("数字: {}".format(num))
print("空格: {}".format(space))
print("其他字符: {}".format(other))
