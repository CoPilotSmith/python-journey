# day 11 -- KYRIEEEE IRVINGGGGG - the guru, the higher self, the conscious one, THE Higher KA

expenses = [1200,450,250,200]

expenses = {
    "rent" : 1200, 
    "food" : 450,
    "transportation" : 250,
    "entertainment" : 200
}

kyrie_stats = {
    "points": 1000, 
    "assist": 2, 
    "jersey_number" : 11,
}

 # the code above creates a list named expenses, this symbol --> { 
 # is being used as a dictionary to assign a name to the numbers in the variable named expenses

 # below we will make an example for KYRIE IRVING 

for key in kyrie_stats:
    if kyrie_stats[key] > 10:
        print(key, kyrie_stats[key])


# for loop retreives the value itself, ex --> in kyrie_stats the stat names are points, assist, and jersey number 
# the kyrie_stat [stat] call retreives the value assosiated with the stat 


for stat in kyrie_stats:
    if kyrie_stats[stat] > 10: 
        print (stat, kyrie_stats[stat]) 















