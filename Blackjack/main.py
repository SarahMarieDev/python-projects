import random
import os
from art import logo

def clear():
    lambda: os.system('clear')

def deal_card():
    """Returns a random card from the deck."""
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_values)
    return card


def calculate_score(cards):
    """Calculates the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(playerScore, houseScore):
    if playerScore > 21 and houseScore > 21:
        return "You went over. You lose. 😤"

    if playerScore == houseScore:
        return "Draw 🙃"
    elif playerScore == 0:
        return "Win with a Blackjack 🥳"
    elif houseScore == 0:
        return "Lose, opponent has Blackjack 😱"
    elif playerScore > 21:
        return "You went over. You lose. 😭"
    elif houseScore > 21:
        return "Opponent went over. You win 😄"
    elif playerScore > houseScore:
        return "You win! 😃"
    else:
        return "You lose. 😢"

def playGame():
    """Start a game of Blackjack"""
    print(logo)

    playerCards = []
    houseCards = []
    is_game_over = False

    for _ in range(2):
        playerCards.append(deal_card())
        houseCards.append(deal_card())

    while not is_game_over:
        playerScore = calculate_score(playerCards)
        houseScore = calculate_score(houseCards)
        print(f"Your cards: {playerCards}, current score: {playerScore}")
        print(f"Computer's first card: {houseCards[0]}")

        if playerScore == 0 or houseScore == 0 or playerScore > 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                playerCards.append(deal_card())
            else:
                is_game_over = True

    while houseScore != 0 and houseScore < 17:
        houseCards.append(deal_card())
        houseScore = calculate_score(houseCards)

    print(f"Your final hand: {playerCards}, final score: {playerScore}")
    print(f"Computer's final hand: {houseCards}, final score: {houseScore}")
    print(compare(playerScore, houseScore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    playGame()






