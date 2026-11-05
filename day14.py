#Day 14 MUGGSY BOGUES - Throw the Lob to Vince Carter for Day 15 

muggsy_stats = {
    "height_inches": 63,
    "assists": 10,
    "steals": 7,
    "jersey_number": 1
}

def get_player_stat(player, stat):
    return player[stat]

muggsy_assists = get_player_stat(muggsy_stats, "assists")

print(muggsy_assists)

tracy_mcgrady = {
    "points": 35,
    "rebounds": 10,
    "assists": 5
}

def get_tmac_stats (tmac, stats): 
    return tmac [stats]
tmacbuckets = get_tmac_stats(tracy_mcgrady, "points")
print (tmacbuckets)

def get_athlete_stats (athlete, stats):
    return athlete [stats]
tmacrebounds = get_athlete_stats(tracy_mcgrady, "rebounds")
print (tmacrebounds)


def get_player_stats (player, stats):
    return player [stats]
muggsypickpocket = get_player_stats (muggsy_stats, "steals")
print (muggsypickpocket)
    