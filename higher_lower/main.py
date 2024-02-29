from game_data import data
from art import logo, vs
import random

print(logo)

def random_choice():
    return random.choice(data)


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, {description}, from {country}"

def check_result(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    score = 0
    account_a = random_choice()
    account_b = random_choice()
    should_continue = True

    while should_continue:
        account_a = account_b
        account_b = random_choice()
        while account_a == account_b:
            account_b = random_choice()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        follower_count_a = account_a['follower_count']
        follower_count_b = account_b['follower_count']

        is_correct = check_result(guess, follower_count_a, follower_count_b)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()



