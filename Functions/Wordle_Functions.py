import random
from collections import Counter

Version = 6.1

def fImportList(file):
    wordlist = open(fr'Functions/{file}.csv', encoding='utf-8-sig')
    wl = wordlist.read().strip().upper()
    wl = wl.split('\n')
    for i in wl:
        if ' ' in i:
            wl.remove(i)        
    return wl

def fCombinedLists():
    wl1 = fImportList('Word List')
    wl2 = fImportList('Word List_2')
    wlt = wl1 + wl2
    wl = list(set(wlt))
    print(f'Word lists loaded and cleaned')
    return wl

def fRandomWord(wl):
    if not wl:
        return wl    
    wl = list(wl)
    sw = random.randint(0,len(wl)-1)
    print(f'Next Word: {wl[sw]}')


def fPuzzleAnswer(puzzleNo):
    fl = fImportList('Word List')
    print(f'Answer: {fl[puzzleNo]}')

def fRemove_from_list(to_be_deleted, original):
    new_list = list(set(to_be_deleted) ^ set(original))
    print(f'Removed: {len(set(to_be_deleted))} words\nWords Remaining: {len(new_list)}') 
    return new_list

def fRemoveBlackLetters(black_letters, word_list):
    if not black_letters:
        return word_list
    wordlist = set(word_list)
    wordlist_to_delete = []
    #Identifies the words with any of the identified black letter
    for word in wordlist:
        if any(letter in word for letter in black_letters.upper()):
            wordlist_to_delete.append(word)
    return fRemove_from_list(wordlist_to_delete, word_list)

def fRemoveYellowLetters(yellow_letters, word_list):
    if not yellow_letters:
        return word_list
    wordlist = set(word_list)
    yllist = [c for c in yellow_letters.upper() if c.isalpha()]
    wordlist_to_delete = []
    for ln in range(0,len(yellow_letters),2):
        yllwword = yellow_letters[0].upper()
        pos = int(yellow_letters[1])-1
        for word in wordlist:
            if yllwword == word[pos]:
                wordlist_to_delete.append(word)
        yellow_letters = yellow_letters[2:]
    for word in wordlist:
        if not any(letter in word for letter in yllist):
            wordlist_to_delete.append(word)
    new_list = fRemove_from_list(wordlist_to_delete, word_list)
    def fValidWordsY(ltr, llist):
        words_to_return = []
        for word in llist:
            if ltr.upper() in word:
                words_to_return.append(word)
        return words_to_return
    for i in yllist:
        new_list = fValidWordsY(i,new_list)
    return new_list


def fRemoveGreeLetters(green_letters, word_list):
    if not green_letters:
        return word_list
    wordlist = set(word_list)
    # words_to_keep = []
    def fValidWords(ltr, indx, llist):
        words_to_return = []
        for word in llist:
            if ltr.upper() == word[indx]:
                words_to_return.append(word)
        return words_to_return
    for ln in range(0,len(green_letters),2):
        grnwords = green_letters[0].upper()
        pos = int(green_letters[1])-1
        wordlist = fValidWords(grnwords, pos, wordlist)
        green_letters = green_letters[2:]
    print(f'Words Remaining: {len(wordlist)}') 
    return wordlist

def fGetRandom(wordlist):
    if not wordlist:
        return wordlist
    alpha = []
    wordlist = list(wordlist)
    for word in wordlist:
        for ltr in word:
            alpha.append(ltr)
    counter = dict(Counter(alpha).most_common())
    focus_letter = str(next(iter(counter.keys())))
    for_random = list(fRemoveBlackLetters(focus_letter, wordlist))
    for_random = list([word for word in for_random if len(set(word)) >= 5])
    # print(f'Next Word: {random.choice(for_random)}')
    sw = random.randint(0,len(wordlist)-1)
    print(f'Next Word: {wordlist[sw]}')