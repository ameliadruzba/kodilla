def palindormy(word:str):
    reverse_word = word[::-1]
    if word == reverse_word:
        return True
    else:
        return False
    
print(palindormy('kajak'))