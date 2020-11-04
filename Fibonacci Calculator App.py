print('\t\tHey there! Welcome to the Fibonacci Calculator App')

num_fib = int(input('\nHow many digits of fibonacci numbers will you like to compute?: '))
fib_num = [1,1]

for n in range(num_fib-2):
    fib = fib_num[n+1] + fib_num[n]
    fib_num.append(fib)
for number in fib_num:
    print(number)
fib_ratio =[]

print('\n\nThe ratios of the fibonacci numbers are: ')

for n in range(len(fib_num)-1):
    ratio = fib_num[n+1] / fib_num[n]
    fib_ratio.append(ratio)
for i in fib_ratio:
    print(i)

print('\n\nThese ratios approach the golden ratio phi which is 1.618...')