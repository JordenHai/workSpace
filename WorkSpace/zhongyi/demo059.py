import random

def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

newline = []

def main():
    arr = ['red', 'green']
    rate = [59,41]

    red_times = 0
    green_times = 0
    for i in range(1000):
        if arr[random_index(rate)] == 'red':
            red_times += 1
            newline.append('red')
            newline.append(',')
        if arr[random_index(rate)] == 'green':
            green_times += 1
            newline.append('green')
            newline.append(',')

if __name__ == '__main__':
    main()