import random

objects_list = ['rock', 'paper', 'scissors']


print('WELCOME TO ROCK PAPER SCISSORS')
def game_on():
	my_wins = 0
	cpu_wins = 0	
	while my_wins < 3 and cpu_wins < 3:
		user_choice = input('Make your choice (rock, paper, scissors):').lower()
		while user_choice not in objects_list:
			user_choice = input('Make your choice (rock, paper, scissors):').lower()

		computer_choice = random.choice(objects_list)
		if user_choice == computer_choice:
			print(f'ITS A TIE, computer chose {computer_choice}')

		elif objects_list[(objects_list.index(user_choice) + 1) % len(objects_list)] == computer_choice:
			print(f'YOU LOST, computer chose {computer_choice}')
			cpu_wins += 1
		else:
			print(f'YOU WON, computer chose {computer_choice}')
			my_wins += 1
		print(f'You scored {my_wins} against {cpu_wins}')
	play_again = input('Do you wanna play again ?').lower()
	if play_again.startswith('y'):
		game_on()
	else: exit('GoodBye')
game_on()