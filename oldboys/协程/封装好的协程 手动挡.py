from greenlet import greenlet
# 在两个协程之间 手动切换 上下文
def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()
    pass

def test2():
    print(56)
    gr1.switch()
    print(78)
    pass

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
