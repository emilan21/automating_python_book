def to_string(list):
    list_string = ''
    for i in range(len(list) - 1):
        list_string += list[i] + ', '

    return list_string + 'and ' + list[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
new_string = to_string(spam)
print(new_string)
