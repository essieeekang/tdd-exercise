VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    if len(hand) > 5:
        return "Invalid"
    
    score = 0
    facecard = ['Jack', 'Queen', 'King']
    ace_count = 0

    for card in hand:
        if card not in VALID_CARDS:
            return "Invalid"
        elif card in facecard:
            score += 10
        elif card == 'Ace':
            ace_count += 1
        else:
            score += card

    if 'Ace' in hand:
        if score + 11 + (ace_count - 1) > 21:
            score += ace_count
        else:
            score += 11 + (ace_count - 1)
    
    if score > 21:
        return "Bust"

    return score
