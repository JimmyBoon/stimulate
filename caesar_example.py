# Caesar Cipher walk through:
#
# Write a program that can encode and decode, using the Caesar Cipher method.
# https://en.wikipedia.org/wiki/Caesar_cipher

# Basically we encode a string by changing its position be a certain value
# and decode it by moving back by that value.

# For example: "my house" adjusted by 1, will be "nz ipvtf"

# Hard to read right?


# Plan for the program:
# A: Encoding:
# 1. Convert the letters to numbers
# 2. Add a adjustment value to the number
# 3. Turn the number back into text.

# B: Decoding
# 1. Convert the letters to numbers
# 2. Minus a adjustment value to the number
# 3. Turn the number back into text.

# Variables:
text_to_be_encoded = "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence."

# 1.
# convert the letters into numbers, so we can add the ajustment:

# Demonostrate looking up a function to convert letters to numbers. The ord() function changes
# letters into unicode(UTF-8), this will meet our purposes for simple conversion.

# https://www.w3schools.com/python/ref_func_ord.asp
# https://en.wikipedia.org/wiki/UTF-8

# Now we have found something that looks like it works, lets do a few tests:

# print(ord('a'))
# print(ord('n'))
# print(ord(' '))
# print(ord('c'))


# Ok, so we can see that the ord() function will do what we require. however doing it like this
# will take ages, and then we still need to move it by a value and then sort it.

# Here we can introduce a loop:

# for character in text_to_be_encoded:
#     print(ord(character))

# Better, but still hard to work with, so better if we add it to a list, we also need to add our adjustment value.

# List to store the encoded numbers:
# encoded_numbers = []

# Value of the adjustment:
# adjustment = 1

# Loop to convert the characters to numbers and apply the adjustment:
# for character in text_to_be_encoded:
#     # while testing/building explain the modulo quickly, with UTF-8 having 256 characters
#     encoded_numbers.append((ord(character) + adjustment) % 256)

# print(encoded_numbers)

# Great so now we have something that is pretty hard to read, but the Caesar Cipher wanted it in letters.
# So now we need another function. chr(), https://www.w3schools.com/python/ref_func_chr.asp to convert numbers back to letters.

# We should test this before using it:
# print(chr(97))

# Now we can build another loop to go over our encoded numbers and convert then back to letters:

# encoded_text_list = []
# for number in encoded_numbers:
#     encoded_text_list.append(chr(number))

# encoded_text = ''.join(encoded_text_list)
# print(encoded_text)

# Great, so I am convinced that it works, so before moving on to the decoder, lets package it
# up into a function:


def encoder(text_to_encode, adjustment):

    # list to store the characters coverted to numbers, with the adjustment.
    encoded_numbers = []

    # Turn the text to be encoded into the numbers with the adjustment
    for character in text_to_encode:
        # while testing/building explain the modulo quickly, with UTF-8 having 256 characters
        encoded_numbers.append((ord(character) + adjustment) % 256)

    # List to store the converted numbers to text
    encoded_text_list = []

    # Turn the numbers into text store it in the above list.
    for number in encoded_numbers:
        encoded_text_list.append(chr(number))

    # Make the list of characters a string
    encoded_text = ''.join(encoded_text_list)

    return encoded_text

# Same as encode but we are reducing by our adjustment:


def decoder(text_to_decode, adjustment):
    adjustment = -adjustment
    return encoder(text_to_decode, adjustment)


# Test our new functions:
# coded_text = (encoder(text_to_be_encoded, 1))
# print(coded_text)

# print(decoder(coded_text, 1))
