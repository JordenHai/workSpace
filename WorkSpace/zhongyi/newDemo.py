
white = 0
black = 1
range_x = 25
range_y = 25

dic_list = []

def readFile(f,dict,value):
   for line in f:
       dict[line[0:-1]] = value

def initArray(dict,start,end,step=1):
    array = []
    for i in range(start,end,step):
        array.append(dict[str(i)])
    return array

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

def indexValue(arr,value,start,end):
    for index in range(start,end):
        arr[index] = value
    return arr

def getLenth(array):
    len = 0
    for index,value in enumerate(array):
        len = index
    return len+1

def updateArray(first,second):

    len = getLenth(first)
    for i in range(0,len,2):
        array = []
        array += first[i:i+2]
        array += second[i:i+2]
        if getLenth(array)>2:
            array = valueArray(array)
            first = indexValue(first, array[0], i, i + 2)
            second = indexValue(second, array[3], i, i + 2)
        else:
            return first, second
    return first,second
    pass

    return first,second

def expandArray()

def fix(range_x,range_y,dict):

    dicts = {}
    arr_list = []
    for index in range(0, range_x * range_y + 1, range_x):
        arr_list.append(index)

    print(arr_list)

    for i in  range(0,range_y-1,4):

        arr1 = initArray(dict, arr_list[i], arr_list[i+1],step=2)
        arr3 = initArray(dict, arr_list[i+2], arr_list[i+3],step=2)

        arr1,arr3 = updateArray(arr1,arr3)
        arr1,arr3 = expandArray(getLenth(array),range_x)
        dic_list.append(arr1)
        dic_list.append(arr3)

def arrayToDict(dict,array,count):
    base = count * getLenth(array)
    for index,value in enumerate(array):
        dict[index] =value

    return dict

def main():
    dic = {}
    dic_fix = {}
    f1 = open("D:\\11", encoding='utf-8')
    f2 = open("D:\\22", encoding='utf-8')

    readFile(f1,dic,white)
    readFile(f2,dic,black)


    # print(dic)
    #
    # arr_list = []
    # for index in range(0,range_x*range_y+1,range_x):
    #     arr_list.append(index)
    #
    # print(arr_list)

    # arr = []
    # for i in range(0,range_x):
    #     if i>=10:
    #         i = i%10
    #         arr.append(i)
    #     else:
    #         arr.append(i)
    # print(arr)
    # for i in range(0,range_y):
    #     print(initArray(dic,arr_list[i],arr_list[i+1]),i)

    fix(range_x,range_y,dic)


if __name__ == '__main__':
    main()
