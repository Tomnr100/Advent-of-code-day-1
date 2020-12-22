r = open('input.txt', 'r')

numbers = []
for number in r:
    number = number.replace('\n', '')
    numbers.append(int(number))

numbers.sort()


l = 0
m = int(len(numbers))-1


lol = True
while lol:
    if numbers[int(l)] + numbers[int(m)] == 2020:
        print('The numbers are:' + str(l) + str(m))
        lol = False
    elif numbers[int(l)] + numbers[int(m)] < 2020:
        l += 1
    elif numbers[int(l)] + numbers[int(m)] > 2020:
        m -= 1

print(numbers[1])
print(numbers[180])