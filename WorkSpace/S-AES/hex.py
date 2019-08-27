SBoxOfN = {'0': '9','1': '4','2': 'A','3': 'B',\
           '4': 'D','5': '1','6': '8','7': '5',\
           '8': '6','9': '2','A': '0','B': '3',\
           'C': 'C','D': 'E','E': 'F','F': '7' }

def yihuo(a,b,c = None):

    ax = int(a,16)
    ay = int(b,16)
    df = ax^ay

    if c==None:
        print(hex(df))
    else:
        az = int(c,16)
        df = df^az
        print(hex(df))

    return hex(df)

def getInteger(valueOfhex):

    pass



