def histogram(word:str):
    group={}
    letters=[]
    for letter in word:
        if letter not in letters:
            letters.append(letter)
        if letter not in group:
            group[letter]=0
        group[letter]+=1
    for letter in letters:
        print(f"{letter} "+group[letter]*"*")

if __name__=="__main__":
    histogram("statistically")