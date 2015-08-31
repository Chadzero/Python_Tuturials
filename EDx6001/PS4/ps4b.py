from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    comp_score = 0
    best_word = None

    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if wordInHand(word, hand):
            # Find out how much making that word is worth
            word_score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if word_score > comp_score:
                best_word = word
                comp_score = word_score

    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
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
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_comp_score = 0

    while calculateHandlen(hand):
        print "Current Hand: ",
        displayHand(hand)
        comp_word = compChooseWord(hand, wordList, n)
        if not comp_word:
            break
        word_score = getWordScore(comp_word, n)
        total_comp_score += word_score
        print "'%s' earned %s points. Total: %s points\n" % (comp_word, word_score, total_comp_score)
        hand = updateHand(hand, comp_word)

    print "Total score: %s points.\n\n" % total_comp_score

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
    hand = None

    while True:
        user_option = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        user_option = user_option.lower()

        if user_option == 'n':
            hand = dealHand(HAND_SIZE)
            while True:
                play_mode = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if play_mode == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                elif play_mode == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print "Invalid Command"

        elif user_option == 'r':
            if hand:
                while True:
                    play_mode = raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if play_mode == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    elif play_mode == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    else:
                        print "Invalid Command"
            else:
                print "You have not played a hand yet. Please play a new hand first!"

        elif user_option == 'e':
            break

        else:
            print "Invalid Command"
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

    # Test cases for compChooseWord
    # print compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)
    # print compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
    # print compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    # print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)

    # Test cases for compPlayHand function
    # compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    # compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    # compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)


