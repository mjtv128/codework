from stack import Stack 

def reverse_string(stack, input):
    for i in range(len(input)):
        stack.push(input[i])
    
    new = ''
    # for i in range(len(input)):
    #     new.append(stack.pop())
    # print('new', ''.join(new))
    while not stack.is_empty():
        new += stack.pop()
    
    return new

stack = Stack()
input = "!evitacudE ot emocleW"
print(reverse_string(stack, input))