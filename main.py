import sys

try:
    first_number = int(sys.argv[1])
except Exception as e:
    first_number = 100
    print(f'First number is not set! Default first_number=100')

try:
    second_number = int(sys.argv[2])
except Exception as e:
    second_number = 195
    print(f'Second number is not set! Default second_number=195')


def get_gmd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number >= second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return first_number or second_number

print(get_gmd(first_number, second_number))

########################################################
# Python include def gcd in math
# Example:
# import math
# math.gcd(40, 36) # >>> 4
#
