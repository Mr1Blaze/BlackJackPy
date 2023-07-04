import random
from art import logo
def clear():
    print('  \n'*100)
def compare(user_score, delear_score):
    if user_score > 21 and delear_score > 21:
        return "You went over. You lose 😤"

    if user_score == delear_score:
        return "Draw 🙃"
    elif delear_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif delear_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > delear_score:
        return "You win 😃"
    else:
        return "You lose 😤"
def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = random.choice(cards)
    return new_card
def score_calc(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)> 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def play_game():
    user_cards = []
    delear_cards = []
    end_game = False
    for i in range(2):
        user_cards.append(random_card())
        delear_cards.append(random_card())
    delear_score = score_calc(delear_cards)
    user_score = score_calc(user_cards)
    print(f'{user_cards} : User cards , User Score is : {user_score}')
    print(f'{delear_cards[0]} : Dealer cards')
    while not end_game:
        if user_score == 0 or delear_score == 0 or user_score > 21:
            end_game = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(random_card())
                user_score = score_calc(user_cards)
                print(f'{user_cards} : User cards , User Score is : {user_score}')
            else:

                end_game = True

    while delear_score != 0 and delear_score < 17 :
        delear_cards.append(random_card())
        delear_score = score_calc(delear_cards)

        end_game = True
    print(f'{user_cards} cartile userului {user_score}')
    print(f'{delear_cards} cartile delearului {delear_score}')
    print(compare(user_score, delear_score))
print(logo)
playing_message='Woould you want to play BlackJack Game? press: "yes" or "no"\n'
while (input(playing_message)) == 'yes':
    clear()
    print(logo)
    play_game()