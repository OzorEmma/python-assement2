#A function code that accepts any number of numbers as positional
#arguments and prints the sum of those numbers

def Sum_Numbers(*numbers):
    Sum=0
    for number in numbers:
        Sum+=number
    return Sum
Result=Sum_Numbers(2,3,5,4,3)
print(f'The sum is {Result}')
    
