# 从键盘获取一行输入字符
s = input()

# 初始化各类字符的计数变量
letter = 0  # 英文字符计数
digit = 0   # 数字计数
space = 0   # 空格计数
other = 0   # 其他字符计数

# 遍历输入的每一个字符
for char in s:
    if char.isalpha():  # 判断是否为英文字符（字母）
        letter += 1
    elif char.isdigit():  # 判断是否为数字
        digit += 1
    elif char.isspace():  # 判断是否为空格
        space += 1
    else:  # 其余的为其他字符
        other += 1

# 按照要求的格式输出结果
print(f"英文字符:{letter}")
print(f"数字:{digit}")
print(f"空格:{space}")
print(f"其他字符:{other}")# 这个文件用于编写代码
