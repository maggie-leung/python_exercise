def getReverse(sentent):
    splited = sentence.split(' ')
    reverse = splited[::-1]
    result = ' '.join(reverse)
    return result

sentence = input('Give a sentence and I will give you the reverse!!')
print(sentence)
print(getReverse(sentence))
