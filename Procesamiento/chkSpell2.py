from textblob import Word

word = Word('smrtph')
result = word.spellcheck()
    
if word == result[0][0]:
    print(f'Spelling of "{word}" is correct!')
else:
    print(f'Spelling of "{word}" is not correct!')
    print(f'Correct spelling of "{word}": "{result[0][0]}" (with {result[0][1]} confidence).')
'''
word = Word('Manzana')
result = word.correct()
print(result)
'''
