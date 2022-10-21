import re


def is_it_palindrom(string):
    string = string.lower()
    reg = re.compile('[^a-zA-Z]')
    string = reg.sub('', string)

    length = len(string)
    length = length // 2
    for i in range(length):
        if string[i] != string[-1 - i]:
            return False
    return True
