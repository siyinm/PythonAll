num1=1
num2=1
print('%d, %d' % (num1, num2), end='')
for i in range(1, 19):
    num1, num2 = num2, num1 + num2
    # tmp=num1
    # num1=num2
    # num2=tmp+num2
    print(', %d' % num2, end='')
