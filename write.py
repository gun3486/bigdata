#i=['홍길동','강감찬','이순신']
i=['홍길동\n','강감찬\n','이순신\n']
f=open('test.txt','w',encoding='utf-8')
f.write('테스트입니다\n')
#f.write(i) #string만 가능 list는 안됨
f.writelines(i) #에러 안남
f.close()

'''
i=['홍길동\n','강감찬\n','이순신\n']
f=open('test.txt','w',encoding='utf-8')
for j in range(3):
 f.write(str(i[j]))
f.close()
'''