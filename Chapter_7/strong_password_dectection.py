#! python3.5
# strong_password_detection.py - Dectects if user supplied password is strong or weak

import re

def passwd_stregth(password):
    passwd_length_regex = re.compile(r'''^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$''')

    if passwd_length_regex.search(password) is None:
        return False
    else:
        return True

print('Enter a password')
passwd = input()
pass_stregth = passwd_stregth(passwd)
if pass_stregth == True:
    print('Your password is strong')
else:
    print('Your password is weak')
