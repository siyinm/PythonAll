from math import sqrt
num = int (input('input a number: '))
end = int(sqrt(num))
isPrime=True
for i in range(2, end+1):
    if num % i==0:
        isPrime=False
        break
if isPrime and num!=1:
    print('%d is prime' % num)
else:
    print('%d is not prime' % num)
