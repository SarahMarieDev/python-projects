import art
from game_data import data
import random

print(art.logo)

# Get a random dictionary from the list
def get_random_dictionary():
    return random.choice(data)

# Compare follower counts
def compare_follower_counts(follower_count_A, follower_count_B):
    if follower_count_A > follower_count_B:
        return "A"
    else:
        return "B"
    
# check if user is correct
def compare_guess(guess, highest):
    if guess == highest:
        return True
    else:
        return False

# make game repeatable
def play_game():
    # keep score
    score = 0
    is_game_over = False
    
    # select random dictionary from data
    random_dict_A = get_random_dictionary()
    
    while is_game_over == False:
        random_dict_B = get_random_dictionary()

        # extract data from dictionary
        name_A = random_dict_A["name"]
        follower_count_A = random_dict_A["follower_count"]
        description_A = random_dict_A["description"]
        country_A = random_dict_A["country"]
        
        name_B = random_dict_B["name"]
        follower_count_B = random_dict_B["follower_count"]
        description_B = random_dict_B["description"]
        country_B = random_dict_B["country"]
            
        # format data into printable format
        print(f"Compare A: {name_A}, a(n) {description_A}, from {country_A}.")
        print(art.vs)
        print(f"Against B: {name_B}, a(n) {description_B}, from {country_B}.")
        
        # ask user for a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        # Check which answer is higher
        highest = compare_follower_counts(follower_count_A, follower_count_B)
        result = compare_guess(guess, highest)
        
        # give user feedback on their guess
        if result == True:
            score = score + 1
            random_dict_A = random_dict_B
            print(f"You're right! Current score: {score}.")
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}.")
        
# Start game
play_game()