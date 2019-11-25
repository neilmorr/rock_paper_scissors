p_1_score = 0
p_2_score = 0
p_1_games_won = 0
p_2_games_won = 0
tie_status = False
exit_flag = 0
player_one = ''
player_two = ''
valid_strings = ['ROCK', 'PAPER', 'SCISSORS']
prompt_one_input_flag = True
prompt_two_input_flag = True

while True:
    while prompt_one_input_flag:  # Loops input prompt for Player One until valid input received.
        player_one = str.upper(input('Your turn, Player One. Please choose "Rock", "Paper" or "Scissors."'))
        if player_one not in valid_strings:
            print('Input not valid. Please re-enter either "Rock", "Paper" or "Scissors."')
        else:
            prompt_one_input_flag = False
        if not prompt_one_input_flag:
            break
    while prompt_two_input_flag:
        player_two = str.upper(input('Your turn, Player Two. Please choose "Rock", "Paper" or "Scissors."'))
        if player_two not in valid_strings:
            print('Input not valid. Please re-enter either "Rock", "Paper" or "Scissors."')
        else:
            prompt_two_input_flag = False
        if not prompt_two_input_flag:
            break
    if player_one == player_two:
        print("It's a tie!")
        tie_status = True
    elif (player_one == 'ROCK') or (player_one == 'ROCK' and player_two == 'PAPER') or (player_one == 'SCISSORS' and player_two == 'ROCK'):
        print("Player Two Wins!")
        p_2_score += 1
    else:
        print("Player One Wins!")
        p_1_score += 1
    if p_1_score < 3 and p_2_score < 3:
        if not tie_status:
            print("Current game score: Player One has {}, and Player Two has {}".format(str(p_1_score), str(p_2_score)))
    elif p_1_score > p_2_score:
        print('Congratulations, Player One. You won the game by a score of {} to {}'.format(str(p_1_score), str(p_2_score)))
        p_1_games_won += 1
        continue_or_quit = str(input('Would you like to play again? Y or N'))
        if continue_or_quit == "N":
            exit = 1
        elif continue_or_quit == "Y":
            print('The current score is as follows: Player One has won {} games, and Player Two has won {} games'.format(str(p_1_games_won), str(p_2_games_won)))
            p_1_score = 0
            p_2_score = 0
    else:
        print('Congratulations, Player Two. You won the game by a score of {} to {}.'.format(str(p_2_score), str(p_1_score)))
        p_2_games_won += 1
        continue_or_quit = str(input('Would you like to play again? Y or N'))
        if continue_or_quit == "N":
            exit = 1
        elif continue_or_quit == "Y":
            print('The current score is as follows: Player One has won {} games, and Player Two has won {} games'.format(str(p_1_games_won), str(p_2_games_won)))
            p_1_score = 0
            p_2_score = 0
    prompt_one_input_flag = True
    prompt_two_input_flag = True
    tie_status = False
    if exit_flag == 1:
        print('Thanks for playing! The final score: Player One won {} games, and Player Two won {} games'.format(str(p_1_games_won), str(p_2_games_won)))
        break



