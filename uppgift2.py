print("\nTELEFONLISTA\n")

f = open('./test.txt', 'r', encoding='utf-8')

rad = f.readline()
while rad:
    print(rad, end='')
    rad = f.readline()
f.close()