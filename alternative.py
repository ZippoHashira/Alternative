# Declare a string variable 'sentence' and store a sentence in it.
# Create a new string variable 'final_sentence' and store an empty string in it.
sentence = input("Enter a sentence: ")
final_sentence = ""

# Create a new variable 'sentence_length' to store the length of 'sentence'.
sentence_length = len(sentence)

# For loop begin, looping through the length of sentence 'sentence_length'.
for letter in range(sentence_length):

    # if letter is divisible by 2 (even number count letter),
    # convert letter to uppercase and store it in the variable 'final_sentence'.
    if letter % 2 == 0:
        final_sentence = final_sentence + sentence[letter].upper()

    # else, convert letter to lowercase and store it in the variable 'final_sentence'.
    else:
        final_sentence = final_sentence + sentence[letter].lower()

# Print 'final_sentence' to display the new sentence with each alternative letters upper and lowercase.
print(final_sentence)

print("\n")

# Split the sentence using .split() and store it in a variable 'sentence_list'.
# Create an empty list and store it in the variable 'new_list'.
# Create new variable 'split_length' to store the length of 'split_sentence'.
sentence_list = sentence.split(" ")
new_list = []
split_length = len(sentence_list)

# For loop begin, for 'word' in range of 'split_length'.
for word in range(split_length):

    # If 'word' is divisible by 2 (even number count word),
    # use .append() function to add the 'sentence_list[word]' to the 'new_list' and convert it to lowercase.
    if word % 2 == 0:
        new_list.append(sentence_list[word].lower())

    # else, use .append() function to add the 'sentence_list[word]' to the 'new_list' and convert it to uppercase.
    else:
        new_list.append(sentence_list[word].upper())

# Use .join() function to join (" ") to the 'new_list' and store it in the variable 'new_sentence'.
new_sentence = " ".join(new_list)

# Print 'new_sentence' to display the new sentence with each alternative word lower and uppercase.
print(new_sentence)
