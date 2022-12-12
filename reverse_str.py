def reverse(str):
    out=""
    for i in range(len(str)):
        out += str[len(str)-i-1]
    return out

str = "Chad is Cool"

print(reverse(str))
