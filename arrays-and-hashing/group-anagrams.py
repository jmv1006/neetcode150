
strings = [""]

def groupAnagrams(strs):
    letterMap = {}

    def count(string):
        ordered = sorted(string)
        letters = {}
        for letter in ordered:
            if(letter in letters):
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        lettersString = str(letters)
        if(lettersString in letterMap):
            letterMap[lettersString].append(string)
        else:
            letterMap[lettersString] = [string]
    
    for string in strs:
        count(string)

    result = []
    for grouping in letterMap:
        result.append(letterMap[grouping])
    return result
    

groupAnagrams(strings)

