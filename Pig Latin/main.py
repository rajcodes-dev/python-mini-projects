"""English to Pig Latin"""
print("Enter the English message to translate into the pig latin: ")
message = input()  # My name is Raj Tiwari and I am 4,000 years old.

VOWELS = ['a','e','i','o','u','y']

pigLatin = []
for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]

    # Remember that the word are in title or upper case
    wasTitle = word.istitle()
    wasUpper = word.isupper()

    word = word.lower() # lower the word for easier translation

    # Separate consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the pig latin at the ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word in upper and title case
    if wasTitle:
        word = word.title()
    if wasUpper:
        word = word.upper()

    # Add non-letter word at the start and the end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the word back together into a single string:
print(' '.join(pigLatin))
