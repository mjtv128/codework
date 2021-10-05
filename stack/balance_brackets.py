from stack import Stack

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


def is_balanced(brackets):
    s = Stack()
    is_balanced = True
    index = 0 

    while index < len(brackets) and is_balanced:
        brac = brackets[index]
        if brac in '({[':
            s.push(brac)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, brac):
                    is_balanced = False
                    break 
        index += 1
    
    if s.is_empty() and is_balanced:
        return True 
    else:
        return False

a = is_balanced('(((}}}}]')
print('a', a)
b = is_balanced('[{()}]')
print('b', b)