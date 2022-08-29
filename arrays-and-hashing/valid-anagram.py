def isAnagram(s, t):
    if(len(s) != len(t)): return False

    sdic = {}

    for letter in s:
        if letter in sdic:
            sdic[letter] += 1
        else: sdic[letter] = 0
    
    for letter in t:
        if letter in sdic:
            if sdic[letter] == 0:
                sdic.pop(letter, None)
            else: sdic[letter] -= 1
    
    if(sdic): return False
    else: return True



s = "rat"
t = "car"

print(isAnagram(s, t))