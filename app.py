from constants import *
from random import choice

roster = PLAYERS.copy()
teams = TEAMS.copy()
cleaned_list = []
experienced_players = []
unexperienced_players = []
number_of_players = [18]
drafted_player = []
final_teams = {}


def set_teams(team_list):
	"""assigns a list of teams to a dictionary"""
	for team in team_list:
		final_teams[team] = []
	return


def clean_list(players):
	"""changes experience strings to booleans, changes integer strings to integers, turns guardians into a list, and moves cleaned information to cleaned_list"""
	for player in players:
		if player['experience'] == 'YES':
			player['experience'] = True
		if player['experience'] == 'NO':
			player['experience'] = False
		split_height = player['height'].split()
		del(split_height[1])
		player['height'] = int(split_height[0])
		player['guardians'] = list(player['guardians'].split('and'))
		cleaned_list.append(player)
	return


def create_even_teams(info):
	"""assign's players to a even team based on experience and number of players"""
	for player in info:
		player_count = len(info)
		if player['experience'] == True:
			experienced_players.append(player)
		if player['experience'] == False:
			unexperienced_players.append(player)
	number_of_players[0] = player_count
	even_team_number = int(number_of_players[0] / 6)
	generate_random_experienced_players('Panthers')
	generate_random_unexperienced_players('Panthers')
	generate_random_experienced_players('Warriors')
	generate_random_unexperienced_players('Warriors')
	generate_random_experienced_players('Bandits')
	generate_random_unexperienced_players('Bandits')


def generate_random_experienced_players(team):
	"""generates three random experienced players"""
	n = 3
	while n != 0:
		random_player = choice(experienced_players)
		if random_player not in drafted_player:
			drafted_player.append(random_player)
			n -= 1
			final_teams[team].append(random_player)
		if random_player in drafted_player:
			continue
	return


def generate_random_unexperienced_players(team):
	"""generates three random unexperienced players"""
	n = 3
	while n != 0:
		random_player = choice(unexperienced_players)
		if random_player not in drafted_player:
			drafted_player.append(random_player)
			n -= 1
			final_teams[team].append(random_player)
		if random_player in drafted_player:
			continue
	return


def display_player_stats(team):
	"""displays players stats based on team"""
	for item in team:
		name = item['name']
		height = item['height']
		experience = item['experience']
		if experience == True:
			experience = "Has experience"
		if experience == False:
			experience = "Doesn't have any experience"
		if len(item['guardians']) != 2:
			print("{}:\n {}\n Is {} inches tall\n Guardians: {}\n".format(name, experience, height, item['guardians'][0]))
		if len(item['guardians']) == 2:
			print("{}:\n {}\n Is {} inches tall\n Guardians: {},{}\n".format(name, experience, height, item['guardians'][0], item['guardians'][1]))
	return


def display_team_stats(team, team_name):
	"""display's a teams stats"""
	player_height = []
	for item in team:
		team_players = len(team)
		team_experienced_players = int(len(experienced_players) / (len(final_teams)))
		team_unexperienced_players = int(len(unexperienced_players) / (len(final_teams)))
		player_height.append(item['height'])
		average_height = (f"{int(sum(player_height) / team_players)} inches")
	print("{}\nTotal team members:{}\nTotal experienced players:{}\nTotal unexperienced players:{}\nAverage height:{}\n".format(team_name, team_players, team_experienced_players,  team_unexperienced_players, average_height, 
		))
	player_height.clear()


def help():
	"""displays command options to the user"""
	print("Enter help to see available commands")
	print("Enter the team name to see team stats")
	print("Enter quit when done looking at team stats")
	print("\n")


def menu():
	"""where the user interacts with the program"""
	active = True
	while active:
		print("~~~Enter the team name for team stats~~~\n~~~Enter quit to end program~~~")
		print("~~~Teams are {}, {}, {}~~~".format(teams[0], teams[1], teams[2],))
		user_input = input("Enter (team name) or (quit): ").lower()
		print('\n')
		if user_input == "panthers":
			display_team_stats(final_teams['Panthers'], "~~Panthers~~:")
			display_player_stats(final_teams["Panthers"])
			continue
		if user_input == "warriors":
			display_team_stats(final_teams['Warriors'], "~~Warriors~~:")
			display_player_stats(final_teams['Warriors'])
			continue
		if user_input == "bandits":
			display_team_stats(final_teams['Bandits'], "~~Bandits~~:")
			display_player_stats(final_teams['Bandits'])
			continue
		if user_input == "help":
			help()
			continue
		if user_input == "quit".lower():
			print("Have a nice day!!!")
			active = False
		else:
			print("command not found, type help for command options\n")
			continue


def main():
	set_teams(teams)
	clean_list(roster)
	create_even_teams(cleaned_list)
	menu()


if __name__ == "__main__":
	main()
	