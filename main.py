# 接收用户输入的一行字符
input_str = input("请输入一行字符：")

# 初始化各类字符的计数器
english_char = 0
number_char = 0
space_char = 0
other_char = 0

# 遍历输入字符串中的每一个字符
for c in input_str:
    # 判断是否为英文字母
    if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
        english_char += 1
    # 判断是否为数字
    elif c >= '0' and c <= '9':
        number_char += 1
    # 判断是否为空格
    elif c == ' ':
        space_char += 1
    # 其余的为其他字符
    else:
        other_char += 1

# 按照指定格式输出统计结果
print(f"英文字符:{english_char}")
print(f"数字:{number_char}")
print(f"空格:{space_char}")
print(f"其他字符:{other_char}")
