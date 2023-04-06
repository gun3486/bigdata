inFp = None    # 입력 파일
inStr = ""        # 읽어온 문자열

inFp = open("D://2023Bigdata/test.txt", "r", encoding='UTF8' )
#inFp = open("C:/Temp/data1.txt", "r")
inStr = inFp.read()
'''
inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
'''
print(inStr, end = "")

inFp.close()

'''
inFp = None	# 입력 파일
inStr = ""		# 읽어온 문자열

inFp = open("D://2023Bigdata/test.txt", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print(inStr, end = "")

inFp.close()
'''
'''
inFp = None
inList = ""

inFp = open("D://2023Bigdata/test.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines() #여러 줄을 리스트로 읽음
print(inList)

inFp.close()
'''
'''
inFp = None
inList, inStr = [], ""

inFp = open("D://2023Bigdata/test.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end="")

inFp.close()
'''

