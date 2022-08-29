from distutils.command.clean import clean


def isPalindrome(s):
    sanitized  = s.lower().replace(" ", "")
    nochars = "".join(e for e in sanitized if e.isalnum())    
    p1 = 0
    p2 = len(nochars) - 1

    while(p1 < p2):
        if(nochars[p1] != nochars[p2]): return False
        p1 += 1
        p2 -= 1

    return True


s = " "
print(isPalindrome(s))