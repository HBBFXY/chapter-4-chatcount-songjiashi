def count_characters():
    # 从键盘输入一行字符
    s = input()
    
    # 初始化计数器
    letters = 0
    digits = 0
    spaces = 0
    others = 0
    
    # 遍历字符串中的每个字符
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  # 英文字母
            letters += 1
        elif '0' <= char <= '9':  # 数字
            digits += 1
        elif char == ' ':  # 空格
            spaces += 1
        else:  # 其他字符
            others += 1
    
    # 严格按照要求格式输出结果
    print("英文字符: {}".format(letters))
    print("数字: {}".format(digits))
    print("空格: {}".format(spaces))
    print("其他字符: {}".format(others))

# 调用函数
if __name__ == "__main__":
    count_characters()
