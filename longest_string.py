# Program to find the longest substring without repeating characters

word = input("Enter a word: ")   # take input from user
longest = ""                     # stores the longest substring found
stop = False                     # flag to stop early if remaining part is too short

# Outer loop: starting index of substring
for i in range(len(word)):
    temp = ""                    # temporary substring
    
    # Optimization: if remaining characters are fewer than current longest, break
    if len(word[i:]) < len(longest):
        stop = True
        break
    
    # Inner loop: build substring from position i
    for j in range(i, len(word)):
        # If character already in temp, break (no repetition allowed)
        if word[j] in temp:
            break
        else:
            temp += word[j]      # add character to temp
        
        # Update longest if temp is longer
        if len(temp) > len(longest):
            longest = temp

# Print the result
print("Longest substring without repetition:", longest)