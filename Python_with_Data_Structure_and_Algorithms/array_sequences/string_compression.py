def compress_string(given):

    # creating empty string for final output
    string_output = ''

    # edge cases
    if len(given) == 0:
        return ''

    if len(given) == 1:
        return s + "1"

    # initializing variables for tracking
    count = 1
    index = 1

    while index < len(given):

        # checking similar chars
        if given[index] == given[index-1]:
            # add the char count
            count += 1
        else:
            # add new char in the output string
            string_output = string_output + given[index-1] + str(count)
            # new char count becomes 1
            count = 1
        # adding index count to loop thorugh
        index += 1
    
    # adding the final running string
    string_output = string_output + given[index-1] + str(count)

    print("Answer: ", string_output)

compress_string('AAAAABBBBCCCC')

        
