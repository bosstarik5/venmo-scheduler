def pattern_matching(string, pattern):
    idxp = idxs = 0
    lenp, lens = len(pattern), len(string)
    while idxs < lens:
        if idxp >= lenp:
            return False
        elif string[idxs] == pattern[idxp]:
            idxp += 1
            idxs += 1
        else:
            if pattern[idxp] == '*':
                while idxs < lens and string[idxs] == string[idxs - 1]:
                    idxs += 1
                idxp += 1
            elif pattern[idxp] == '.':
                idxp += 1
                idxs += 1
            elif pattern[idxp + 1:]:
                if pattern[idxp + 1] == '*':
                    idxp += 2

    while idxp < lenp:
        if pattern[idxp] == '*':
            idxp += 1
        elif idxp + 1 < lenp:
            if pattern[idxp + 1] == '*':
                idxp += 2
            else:
                return False
        else:
            return False
    return True


print(pattern_matching("abc", "abc") == True)

# Dots:
print(pattern_matching("", ".") == False)

print(pattern_matching("abb", "a.") == False)
print(pattern_matching("", "ab.") == False)
print(pattern_matching("abc", "") == False)
#Stars:
print(pattern_matching("abbbbc", "ab*c") == True)

print(pattern_matching("aa", "a*") == True)

print(pattern_matching("", "*") == True)
print(pattern_matching("ab", "a*") == False)
print(pattern_matching("", "a*") == True)
print(pattern_matching("b", "a*b") == True)

# Both:
print(pattern_matching("abbbbc", "a.*c") == True)
print(pattern_matching("abbbbc", "a.*cd") == False)
print(pattern_matching("abbbbcd", "a.*cd") == True)
