import string

def word_frequency(sentence):
    words = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
