from collections import defaultdict

# create a function to decide what type a hand is
# create a function to compare 2 hands and see who has the first higher card
# create a function to compare 2 hands and decide which is stronger
    # which will consist of, first: decide what the strong type is, and if equal, decide which has the strongest first card
# create a sorting function that takes a list of hands,bid combos and sorts/ranks them by strength
# create a function that takes a list of hands,bid combos and computes the total winnings

def main():
    hand_bids = read_file('input.txt')

    sorted = sort_hand_bids(hand_bids)

    tw = total_winnings(sorted)

    answer = tw
    print(f'The answer: {answer}')

def total_winnings(sorted_hand_bids):
    total_winnings = 0
    for i, hand_bid in enumerate(sorted_hand_bids):
        total_winnings += (i+1) * hand_bid[1]

    return total_winnings
def sort_hand_bids(hand_bids):
    sorted = [hand_bids[0]]

    for hand_bid in hand_bids[1:]:
        hand = hand_bid[0]
        bid = hand_bid[1]

        inserted = False
        for s, hand_bid_s in enumerate(sorted):
            hand_s = hand_bid_s[0]
            bid_s = hand_bid_s[1]

            strongest_hand = compare_hands(hand, hand_s)

            if strongest_hand == hand_s: # sort from weak to strong
                sorted.insert(s, hand_bid)
                inserted = True
                break

        if not inserted: # strongest hand at that point
            sorted.append(hand_bid)

    return sorted

def hand_type(hand):
    if number_of_kinds(hand) == 5:
        return ('five_of_a_kind', 6)
    elif number_of_kinds(hand) == 4:
        return ('four_of_a_kind', 5)
    elif is_full_house(hand):
        return ('full_house', 4)
    elif number_of_kinds(hand) == 3:
        return ('three_of_a_kind', 3)
    elif is_two_pair(hand):
        return ('two_pair', 2)
    elif number_of_kinds(hand) == 2:
        return ('one_pair', 1)
    else:
        return ('high_card', 0)

def compare_hands(hand1, hand2):
    type_hand1 = hand_type(hand1)
    type_hand2 = hand_type(hand2)

    if type_hand1[1] > type_hand2[1]:
        return hand1
    elif type_hand1[1] < type_hand2[1]:
        return hand2
    else:
        return compare_first_highest_card(hand1, hand2)
def compare_first_highest_card(hand1, hand2):
    for i in range(0, len(hand1)):
        c = compare_card(hand1[i], hand2[i])
        if c is not None:
            if c == hand1[i]:
                return hand1
            else:
                return hand2

def compare_card(card1, card2):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    if order.index(card1) > order.index(card2):
        return card1
    elif order.index(card2) > order.index(card1):
        return card2
    else:
        return None

def number_of_kinds(hand):
    kinds = defaultdict(int)
    cards = list(hand)

    max_number_of_kinds = 0

    for card in cards:
        kinds[card] += 1
        max_number_of_kinds = max(max_number_of_kinds, kinds[card])

    return max_number_of_kinds

def is_full_house(hand):
    kinds = defaultdict(int)
    cards = list(hand)

    for card in cards:
        kinds[card] += 1

    keys = list(kinds.keys())
    if len(keys) == 2:
        if (kinds[keys[0]] == 2 and kinds[keys[1]] == 3) or (kinds[keys[0]] == 3 and kinds[keys[1]] == 2):
            return True
    return False

def is_two_pair(hand):
    kinds = defaultdict(int)
    cards = list(hand)

    for card in cards:
        kinds[card] += 1

    number_of_pairs = 0
    for card in kinds.keys():
        if kinds[card] == 2:
            number_of_pairs += 1
    return number_of_pairs == 2

def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    hand_bids = []
    for line in lines:
        hand, bid = line.split()
        hand_bids.append((hand, int(bid)))

    return hand_bids


if __name__ == "__main__":
    main()
