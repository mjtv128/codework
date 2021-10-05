# Convert Decimal Integer to Binary
# required to use the stack data structure to convert integer 
# values to their binary equivalent.

from stack import Stack 

def convert(stack, decimal):
    # remainder

    if decimal == 0:
        return 0 

    while decimal / 2 != 0:
        print('decimal', decimal)
        remainder = decimal % 2

        decimal = decimal // 2 
        print('remainder', remainder)
        stack.push(remainder)
    
    print('stack', stack.get_stack())
    res = ''
    while not stack.is_empty():
        res += str(stack.pop())
    
    print('res', res)
    return res


stack = Stack()
print(convert(stack, 242))