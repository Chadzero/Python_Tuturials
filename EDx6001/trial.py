def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    hand_count = 0
    for key in hand:
        hand_count += hand[key]
    return hand_count


print calculateHandlen({'a':1,'b':4,'c':1})