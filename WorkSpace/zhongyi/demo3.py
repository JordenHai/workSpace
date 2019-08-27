import math

dic = {}
com_dic = {}
white = 0
black = 1
range_x = 25
range_y = 25

def readFile(f,value):
   for line in f:
       dic[line[0:-1]] = value

def writFile(fileNameBlack,fileNameWhite):
    f1 = open(fileNameBlack, 'w', encoding='utf-8')
    count1 = 0
    f2 = open(fileNameWhite, 'w', encoding='utf-8')
    count2 = 0
    for index,value in com_dic.items():
        if value == white:
            f1.seek(count1)
            f1.write(str(index))
            f1.write("\n")
            count1 = f1.tell()
        else:
            f2.seek(count2)
            f2.write(str(index))
            f2.write("\n")
            count2 = f2.tell()

def initArray(dict,start,end):
    array = []
    for i in range(start,end):
        array.append(dict[str(i)])
    return array

def initDict(array,count):
    base = count * range_x
    for index,value in enumerate(array):
        num = int(base + index)
        com_dic[num] = value


def makeValue(array):
    sum = 0
    for value in array:
        sum +=value
    return sum

def valueArray(array):
    res = makeValue(array)
    if res >= 3:
        return colorArray(array,black)
    elif res <= 1:
        return colorArray(array,white)
    else:
        if array[0] == array[2]:
            return colorArray(array,white)
        else:
            return colorArray(array,black)

def colorArray(array,value):
    for index,ele in enumerate(array):
        array[index] = value
    return array

def updateArray(firstLine,secondLine):
    array = []
    if range_y%2 == 1:
        for i in range(0,range_y-1,2):
            array.append(firstLine[i])
            array.append(firstLine[i+1])
            array.append(secondLine[i])
            array.append(secondLine[i+1])
            array = valueArray(array)

            firstLine[i]    = array[0]
            firstLine[i+1]  = array[1]
            secondLine[i]   = array[2]
            secondLine[i+1] = array[3]

            array = []
    else:
        for i in range(0, range_y, 2):
            array.append(firstLine[i])
            array.append(firstLine[i + 1])
            array.append(secondLine[i])
            array.append(secondLine[i + 1])
            array = valueArray(array)

            firstLine[i] = array[0]
            firstLine[i + 1] = array[1]
            secondLine[i] = array[2]
            secondLine[i + 1] = array[3]

            array = []
    return firstLine,secondLine

def fixArray(x,y):
    arr = []
    array = []
    sumEle = x*y

    for i in range(0,sumEle+1,x):
        arr.append(i)

    print(arr)

    if y%2 == 1:
        for i in range(0,y-1,2):
            arr1 = initArray(dic,arr[i],arr[i+1])
            arr2 = initArray(dic,arr[i+1],arr[i+2])
            arr1,arr2 = updateArray(arr1,arr2)
            array = arr1 +arr2
            initDict(array,i)
            array = []
        array = initArray(dic,arr[-1]-x,arr[-1])
        # print(arr[-1]-x,arr[-1])
        # print(array)
        initDict(array,y-1)

    else:
        for i in range(0, y, 2):
            arr1 = initArray(dic, arr[i], arr[i + 1])
            arr2 = initArray(dic, arr[i + 1], arr[i + 2])
            arr1, arr2 = updateArray(arr1, arr2)
            array = arr1 + arr2
            initDict(array, i)
            array = []

def main():
    f_red = open("D:\\red", encoding='utf-8')
    f_green = open("D:\\green", encoding='utf-8')
    readFile(f_red,white)
    readFile(f_green,black)
    fixArray(range_x,range_y)
    f1 = "D:\\11"
    f2 = "D:\\22"
    print(com_dic)
    writFile(f1,f2)


if __name__ == '__main__':
    main()
