# Largest continous sum

def conti_sum(arr1):

    if len(arr1)==0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr1[1:]:

        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


arr = [2,3,1,4,5,5,3,6,7]
print ("Largest continous sum answer: ", conti_sum(arr))

# ---------------------------------------------------
# Sentence reverse

def rev_word(str):
    
    words = []
    spaces = [' ']
  
    index_tracker = 0
    
    while index_tracker < len(str):
        
        if str[index_tracker] not in spaces:
            word_start = index_tracker
            
            while index_tracker < len(str) and str[index_tracker] not in spaces:
                index_tracker += 1
            
            words.append(str[word_start:index_tracker])
        
        index_tracker += 1
        
    return " ".join(reversed(words))


print("Sentence reverse answer: ", rev_word('   Hello John    how are you   '))