# The Collatz Sequence

def collatz(number):
    remander = number % 2

    if remander == 0:
        anwser = number // 2
        print(anwser)
        return anwser
    elif remander == 1:
        anwser = 3 * number + 1
        print(anwser)
        return anwser

print('Enter a number')
number = int(input())

while number != 1:
    number = collatz(number)
