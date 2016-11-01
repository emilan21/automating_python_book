# The Collatz Sequence

def collatz(number):
    remander = number % 2

    if remander == 0:
        print(str(number // 2))
        return number // 2
    if remander % 2 == 1:
        print(str(3 * number + 1))
        return 3 * number + 1

print('Enter a number')
number = int(input())

while True:
    anwser = collatz(number)
    if anwser == 1:
        break;
