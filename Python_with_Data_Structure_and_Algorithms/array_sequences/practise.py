# 1. Anagram check

def anagram_check(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # edge case if both are different length