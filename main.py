import random

CHOICE_ALIASES = {"s": "snake", "w": "water", "g": "gun"}
VALID_CHOICES = tuple(CHOICE_ALIASES.keys())
# Pairs where the first beats the second
PLAYER_WINS = {("s", "w"), ("w", "g"), ("g", "s")}


def decide_winner(player_choice: str, computer_choice: str) -> str:
    if player_choice == computer_choice:
        return "draw"
    return "win" if (player_choice, computer_choice) in PLAYER_WINS else "lose"


def get_user_choice() -> str:
    prompt = "Choose [s]nake, [w]ater, [g]un or [q]uit: "
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("q", "quit", "exit"):
            return "q"
        if raw in VALID_CHOICES:
            return raw
        print("Invalid choice. Please enter s, w, g, or q.")


def play_round() -> str:
    player = get_user_choice()
    if player == "q":
        return "quit"
    computer = random.choice(VALID_CHOICES)
    result = decide_winner(player, computer)
    print(f"You chose {CHOICE_ALIASES[player]}, computer chose {CHOICE_ALIASES[computer]}.")
    if result == "win":
        print("You win this round!")
    elif result == "lose":
        print("You lose this round.")
    else:
        print("This round is a draw.")
    return result


def main() -> None:
    print("Snake-Water-Gun Game")
    print("--------------------")
    player_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        outcome = play_round()
        if outcome == "quit":
            break
        rounds_played += 1
        if outcome == "win":
            player_score += 1
        elif outcome == "lose":
            computer_score += 1

        print(f"Score -> You: {player_score} | Computer: {computer_score} | Rounds: {rounds_played}\n")

    print("\nFinal Score")
    print(f"You: {player_score} | Computer: {computer_score} | Rounds: {rounds_played}")
    if player_score > computer_score:
        print("Overall result: You win! 🎉")
    elif player_score < computer_score:
        print("Overall result: You lose. 👀")
    else:
        print("Overall result: It's a draw.")


if __name__ == "__main__":
    main()
