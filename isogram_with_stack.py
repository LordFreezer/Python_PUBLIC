def is_isogram(string):
    stack = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    popped = []
    for i in string:
        if(any(ele == i or ele.upper() == i for ele in stack)):
                stack.remove(i.lower())
                popped.append(i)                
    if(len(popped) == len(string)):
        return True
    else:
        return False
