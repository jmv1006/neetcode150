def lengthOfLongestSubstring(s):
    if(not s): return 0
    elif(len(s) < 2): return 1
    p1 = 0
    p2 = 1
    max_length = 1

    while(p2 < len(s)):
        chars = [] 
        ##for this current window, check if it has a duplicate
        for x in range(p1, p2 + 1):
            if(s[x] not in chars):
                chars.append(s[x])
            elif s[x] in chars:
                chars = []
        
        if chars:
            max_length = max(max_length, len(chars))
            p2 += 1
        else:
            p1 += 1
    
    return max_length
    

string = "abcabcbb"
print(lengthOfLongestSubstring(string))
