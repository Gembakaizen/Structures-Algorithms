# Structures-Algorithms

Question 1: Implement a function is_balanced(expression) that takes a string 
containing parentheses, curly braces, and square brackets,and determines whether 
the expression is balanced. 

An expression is considered balanced if each opening bracket has a corresponding closing 
bracket in the correct order.

sample input = 

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False 


Sequences (Lists/Tuples): 

Question 2: Write a function remove_duplicates(sequence) that takes a 
sequence (list or tuple) and returns a new sequence with duplicates 
removed while maintaining the original order of elements. 

sample input = 

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]


Dictionaries: 

Question 3: Implement a function word_frequency(sentence) that takes 
a sentence and returns a dictionary containing the frequency of each 
word in the sentence. 

Ignore punctuation and consider words in a case-insensitive manner. 

sample input = 

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)


is_balanced.py
The is_balanced function checks if a given expression has balanced parentheses, curly brackets, and square brackets.

sentence.py
The remove_duplicates function takes a sequence as input and returns a new sequence with duplicate elements removed.
# test case 
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

word_frequency
The word_frequency function takes a sentence as input and returns a dictionary that contains the frequency of each word in the sentence.
# test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
