import requests as req

token = "R3rads14BluiRFD23plSvakR0ohroo4pX1Z92QhYb6cEP-7wZGA"

def get_team_id(team):
    r = req.get(f'https://api.pandascore.co/csgo/teams?search[name]={team}&token={token}')
    team = r.json()
    return team[-1]['id']

def get_team_matches(team_id):
    team_matches = []
    #r = req.get(f"https://api.pandascore.co/csgo/matches/past?page[size]=100?range[begin_at]={start_date},{end_date}&token={token}")
    r = req.get(f"https://api.pandascore.co/csgo/matches/past?filter[opponent_id]={team_id}&token={token}")
    matches = r.json()

    for match in matches:
        team_matches.append(match)

    return team_matches

def prev_encounters(team1_id, team2_id):
    r = req.get(f"https://api.pandascore.co/csgo/matches/past?filter[opponent_id]={team1_id, team2_id}&token={token}")
    matches = r.json()
    for match in matches:
        print("match")
    # team1_matches = get_team_matches(team1_id)
    # team2_matches = get_team_matches(team2_id)
    # team1_wins = 0
    # team2_wins = 0
    # draws = 0
    # for t1_match in team1_matches:
    #     #opponent = t1_match['opponents'][1]
    #     if get_team_id(t1_match['opponents'][1]['opponent']['name']) == team2_id:
    #         print("match")

def calculate_WL(team_id):
    matches = get_team_matches(team_id)
    win = 0
    loss = 0
    draw = 0
    for match in matches:
        if match['draw']:
            draw+=1
        elif match['winner_id'] == team_id:
            win+=1
        else:
            loss+=1
    return {"wins": win, "loss": loss, "draw": draw, "ratio": win/loss}

#liquid_matches = get_team_matches(get_team_id("liquid"))
# liquid_WL = calculate_WL(get_team_id("liquid"))
#prev_encounters(get_team_id("liquid"), get_team_id("vitality"))
print(f'{get_team_id("liquid")}, {get_team_id("vitality")}')
