# read data
poker_file = open('files/p054_poker.txt','r')
poker_file = poker_file.read()
poker_file = str(poker_file)
poker_file = poker_file.replace(',',' ')
poker_file = poker_file.replace('"','')
cards_arr = poker_file.split()

values_ordered = ['2','3','4','5','6','7','8','9','T','J','Q','K','A'] # J = Jack, Q = Queen, K = King, A = Ace
ranks = ['high_card', 'one_pair', 'two_pairs', 'three_of_a_kind', 'straight', 'flush', 'full_house', 'four_of_a_kind', 'straight_flush', 'royal_flush']
games_arr = []
hand_one_arr = []
hand_two_arr = []
counter = 1
player_one_wins = 0
player_two_wins = 0

# rearrange data to an array consisting of game-arrays
for card in cards_arr:
    if counter > 5:
        hand_two_arr.append(card)
    else:
        hand_one_arr.append(card)
    if counter == 10:
        game = [hand_one_arr,hand_two_arr]
        games_arr.append(game)
        counter = 0
        hand_one_arr = []
        hand_two_arr = []
    counter += 1

# returns the highest card of the hand
def getHighCard(game: list):
    highest_ind = 0
    for card in game:
        ind = values_ordered.index(card[0])
        if ind > highest_ind:
            highest_ind = ind
    highest_card = values_ordered[highest_ind]
    return highest_card

# returns pairs (one pair or two pairs) of the hand
def sameCards(game: list):
    hist = []
    pairs = []
    three = []
    four = []
    for card in game:
        if card[0] in hist:
            if card[0] in pairs:
                if card[0] in three:
                    four.append(card[0])
                else:
                    three.append(card[0])
            else:
                pairs.append(card[0])
        else:
            hist.append(card[0])
    if len(four) >= 1: # Four of a Kind found
        return ['4',four[0]]
    elif len(three) == 1: # Three of a Kind or Full House
        for pair in pairs:
            if pair != three[0]:
                full_house_str = three[0] + pair
                return ['3-2',full_house_str]
        return ['3', three[0]]
    elif len(pairs) == 1: # One Pair
        return ['2',pairs[0]]
    elif len(pairs) == 2: # Two Pairs
        return ['2-2',pairs[0],pairs[1]]
    else:
        return 0

# Checks a Flush and requisites for Royal Flush and Straight Flush
def sameSuit(game: list):
    suit = game[0][1]
    for card in game:
        if card[1] != suit:
            return False
    return True

# Cecks Straights and requisites for Straight Flush and Royal Flush
def consecutiveValues(game: list):
    indx_arr = []
    for card in game:
        index = values_ordered.index(card[0])
        if index in indx_arr:
            return False
        else:
            indx_arr.append(index)
    indx_arr = sorted(indx_arr)
    previous_index = 0
    counter = 0
    for index in indx_arr:
        counter += 1
        if counter == 1:
            previous_index = index
        else:
            if index-previous_index != 1:
                return False
            else:
                previous_index = index
    return True

# main loop
for game in games_arr:

    hands_counter = 0
    rank_player_one = 0
    sign_card_player_one = ''
    rank_player_two = 0
    sign_card_player_two = ''

    for hand in game:

        hands_counter += 1
        highest_card = getHighCard(hand)
        rank = ''
        sign_card = ''
        same_cards = sameCards(hand)
        has_same_cards = True
        if same_cards == 0:
            has_same_cards = False
        
        if consecutiveValues(hand) and highest_card == 'A' and sameSuit(hand): # Check a Royal Flush
            rank = 'royal_flush'
        elif consecutiveValues(hand) and sameSuit(hand): # Check a Straight Flush
            rank = 'straight_flush'
        elif has_same_cards and same_cards[0] == '4': # Check a Four of a Kind
            rank = 'four_of_a_kind'
            sign_card = sameCards(hand)[1]
        elif has_same_cards and same_cards[0] == '3-2': # Check a Full House
            rank = 'full_house'
            sign_card = sameCards(hand)[1]
        elif sameSuit(hand): # Check a Flush
            rank = 'flush'
        elif consecutiveValues(hand): # Check a Straight
            rank = 'straight'
        elif has_same_cards and same_cards[0] == '3': # Check a Three of a Kind
            rank = 'three_of_a_kind'
            sign_card = sameCards(hand)[1]
        elif has_same_cards and same_cards[0] == '2-2':
            rank = 'two_pairs'
            sign_card = sameCards(hand)[1]
        elif has_same_cards and same_cards[0] == '2':
            rank = 'one_pair'
            sign_card = sameCards(hand)[1]
        
        if hands_counter == 1: # Player one
            rank_player_one = rank
            sign_card_player_one = sign_card
        else:
            rank_player_two = rank
            sign_card_player_two = sign_card
    
    # Check which player has won the game
    print(game)
    if rank_player_one != '' and rank_player_two != '':
        if ranks.index(rank_player_one) > ranks.index(rank_player_two):
            player_one_wins += 1
        elif ranks.index(rank_player_two) > ranks.index(rank_player_one):
            player_two_wins += 1
        else: # tie - look at card's ranks
            if values_ordered.index(sign_card_player_one[0]) > values_ordered.index(sign_card_player_two[0]):
                player_one_wins += 1
            elif values_ordered.index(sign_card_player_two[0]) > values_ordered.index(sign_card_player_one[0]):
                player_two_wins += 1
            else:
                if rank_player_one == 'full_house' or rank_player_one == 'two_pairs':
                    if values_ordered.index(sign_card_player_one[1]) > values_ordered.index(sign_card_player_two[1]):
                        player_one_wins += 1
                    elif values_ordered.index(sign_card_player_two[1]) > values_ordered.index(sign_card_player_one[1]):
                        player_two_wins += 1
                else:
                    if values_ordered.index(getHighCard(game[0])) > values_ordered.index(getHighCard(game[1])):
                        player_one_wins += 1
                    elif values_ordered.index(getHighCard(game[1])) > values_ordered.index(getHighCard(game[0])):
                        player_two_wins += 1
    elif rank_player_one != '' and rank_player_two == '':
        player_one_wins += 1
    elif rank_player_one == '' and rank_player_two != '':
        player_two_wins += 1
    elif rank_player_one == '' and rank_player_two == '':
        if values_ordered.index(getHighCard(game[0])) > values_ordered.index(getHighCard(game[1])):
            player_one_wins += 1
        elif values_ordered.index(getHighCard(game[1])) > values_ordered.index(getHighCard(game[0])):
            player_two_wins += 1
            
    print(game,' ',player_one_wins,' ',rank_player_one,' ',player_two_wins,' ',rank_player_two)


print('# Wins of player 1: ', str(player_one_wins))
print('# Wins of player 2: ', str(player_two_wins))