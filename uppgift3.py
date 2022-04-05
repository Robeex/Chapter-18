import random

f = open('./slump.txt', 'w', encoding='utf-8')
num=[]
i=0
while i <= 20:
    num= random.sample(range(0,100),1)
    print(num)
    i
    #f.write(num+'\n')
f.close











    
