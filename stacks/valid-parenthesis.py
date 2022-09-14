
def isValid(s):
    pairs = {"{": "}", "(": ")", "[": "]"}
    if(len(s) < 2): return False

    stack = []

    for char in s:
        if char in pairs :
            ##if it is an opening character
            stack.append(char)
        elif stack:
            ##else if it is not an opening character AND stack is populated
            t = stack.pop()
            if(pairs[t] != char):
                return False
        else:
            ##else if it is not an opening character and stack is empty, we know it has no partner
            return False
    
    return True if not stack else False


s="(){}("
isValid(s)