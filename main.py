import random

# Player performance data (example values)
man_city_players = {
    'player1': {'goals': 20, 'assists': 10, 'passing_accuracy': 80, 'defensive_contributions': 50, 'form': 8},
    'player2': {'goals': 15, 'assists': 5, 'passing_accuracy': 85, 'defensive_contributions': 60, 'form': 7},
    # Add more players and their performance data
}

inter_milan_players = {
    'player1': {'goals': 18, 'assists': 8, 'passing_accuracy': 82, 'defensive_contributions': 55, 'form': 9},
    'player2': {'goals': 12, 'assists': 10, 'passing_accuracy': 88, 'defensive_contributions': 58, 'form': 8},
    # Add more players and their performance data
}

# Team strategies (example values)
man_city_strategy = {'formation': '4-3-3', 'pressing': 'high', 'possession': '60%', 'tactics': 'attacking'}
inter_milan_strategy = {'formation': '3-5-2', 'pressing': 'medium', 'possession': '55%', 'tactics': 'counter-attacking'}

# Calculate performance scores for players
def calculate_performance_score(player):
    score = (
        player['goals'] * 0.3 +
        player['assists'] * 0.2 +
        player['passing_accuracy'] * 0.1 +
        player['defensive_contributions'] * 0.1 +
        player['form'] * 0.3
    )
    return score

# Calculate overall team score
def calculate_team_score(players, strategy):
    performance_scores = [calculate_performance_score(player) for player in players.values()]
    average_performance = sum(performance_scores) / len(performance_scores)
    team_score = (
        average_performance * 0.5 +
        random.uniform(0, 10) * 0.3 +  # Add random factor for variation
        random.uniform(0, 10) * 0.2    # Add random factor for variation
    )
    return team_score

# Evaluate past records (example values)
man_city_past_records = {'success_rate': 80, 'previous_encounters': 5, 'performance_under_pressure': 70}
inter_milan_past_records = {'success_rate': 75, 'previous_encounters': 4, 'performance_under_pressure': 75}

# Calculate overall team scores
man_city_score = (
    calculate_team_score(man_city_players, man_city_strategy) +
    man_city_past_records['success_rate'] * 0.2 +
    man_city_past_records['previous_encounters'] * 0.2 +
    man_city_past_records['performance_under_pressure'] * 0.3
)

inter_milan_score = (
    calculate_team_score(inter_milan_players, inter_milan_strategy) +
    inter_milan_past_records['success_rate'] * 0.2 +
    inter_milan_past_records['previous_encounters'] * 0.2 +
    inter_milan_past_records['performance_under_pressure'] * 0.3
)

# Select the best team
if man_city_score > inter_milan_score:
    best_team = 'Manchester City'
else:
    best_team = 'Inter Milan'

# Print the result
print("Champions League Final: Manchester City vs. Inter Milan")
print("===============================================")
print("Team Scores:")
print("Manchester City: {:.2f}".format(man_city_score))
print("Inter Milan: {:.2f}".format(inter_milan_score))
print("===============================================")
print("The best team for the Champions League Final is:", best_team)

