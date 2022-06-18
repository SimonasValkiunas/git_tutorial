number = input('write a number: ')
print('number is: ' + number)
prime = []
for x in range(2, int(number)+1):
    is_prime = True
    for y in range(2, x):
        if x % y == 0:
            is_prime = False
            break
    if is_prime == True:
        prime.append(x)
print(prime)
