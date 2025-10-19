def count_characters():
    try:
        # 从键盘输入一行字符
        s = input().rstrip('\n')  # 去除末尾的换行符
        
        # 初始化计数器
        letters = 0
        digits = 0
        spaces = 0
        others = 0
        
        # 遍历字符串中的每个字符
        for char in s:
            if char.isalpha():  # 英文字母
                letters += 1
            elif char.isdigit():  # 数字
                digits += 1
            elif char.isspace():  # 空格（包括制表符等）
                spaces += 1
            else:  # 其他字符
                others += 1
        
        # 输出结果
        print("英文字符: {}".format(letters))
        print("数字: {}".format(digits))
        print("空格: {}".format(spaces))
        print("其他字符: {}".format(others))
        
    except Exception as e:
        print("发生错误:", e)

# 运行程序
if __name__ == "__main__":
    count_characters()
