from ps4a import *
import time
HAND_SIZE=30
n=HAND_SIZE
#
#
# Problem #6: Computer chooses a word
#
#
def isValidWord(word, hand):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    word.lower()
    newHand=hand.copy()
    for char in word:
        if word.count(char) > hand.get(char,0):
            return False
    return True
def compChooseWord(hand, wordList):

    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """

    totalScore=0
    score=0
    bestWord=None
    for word in wordList:
        if isValidWord(word, hand):
            if getWordScore(word, n)>score:
                bestWord=word
                score=getWordScore(bestWord, n)
    return bestWord
            
            
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    getPoints=0
    points=0
    word='asdf'
    lettersLeft=calculateHandlen(hand)
    while lettersLeft>0:
        print 'Current Hand: '
        displayHand(hand)
        word=compChooseWord(hand, wordList)
        if word == None:
            break
        getPoints=getWordScore(word, n)
        points+=getPoints
        print ('"'+word+'" earned '+str(getPoints)+' points. Total: '+\
        str(points)+' points.' )
        print
        # Update the hand
        hand = updateHand(hand,word)
        lettersLeft=calculateHandlen(hand)
    print 'Total score:',points,'points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    ans=''
    newGame=True
    hand={}
    myHand={}
    while ans != 'e':
        ans2=''
        ans=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if ans == 'n':
            newGame=False
            hand=dealHand(HAND_SIZE)
            
        elif ans == 'r':
            if newGame :
                print 'You have not played a hand yet. Please play a new hand first!'
                continue
            print
        elif ans == 'e':
            break
        else:
            print 'Invalid command.'
            continue
        myHand=hand.copy()
        while ans2 != 'b' or ans2 != 'c':
            ans2=raw_input('Enter u to play yourself, c to let computer play:')
            break
        if ans2=='u':
            playHand(myhand, wordList, HAND_SIZE)
            break
        else:
            compPlayHand(hand, wordList)
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


