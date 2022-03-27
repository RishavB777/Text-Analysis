"""
1. Importing the text
2. Convert the text into lower case
3. Cleaning the text from all the punctuations
"""


import string
text = open('text.txt',encoding='utf-8').read()
print(text)

lower_case = text.lower()

print(lower_case)

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
# str.maketrans()
"""
str1: List of characters that need to be replaced
str2: List of characters with which the characters need to be replaced
str3: List of characters that needs to be deleted

returns: translation table which specifies the conversions that can be used by str.translate()
"""
print(cleaned_text)