fname=input('Enter file name:')
try:
    with open(fname) as fh:
        wordlist=list()
        for line in fh:
            linewords=line.split()
            for word in linewords:
                if word not in wordlist:
                    wordlist.append(word)
    wordlist.sort()
except:
    print('Invalid filename')
print(wordlist)