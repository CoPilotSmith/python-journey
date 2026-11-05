#Day 13 Steve Nash dropping dimes to Amare S. and Raja Bell

nash_stats = {
    "points" : 156,
    "assists": 13,
    "jersey_number": 13,
    "rebounds": 8
}

print (nash_stats)

# created a dictionary named Steve Nash, it holds the stats --> points, assists, jersey number, and rebounds

for stat in nash_stats:
    if nash_stats[stat] > 13:
        print (stat, nash_stats[stat])

# for loop that checks the value assosiated with each stat, if that stat is greater than 13 then it will 
# print the stat and the value assosiated with it. EX above will only return points because its the only 
# stat greater than 13

high_stat_count = 0

for stat in nash_stats:
    if nash_stats[stat] >= 13:
        high_stat_count += 1

print(high_stat_count)

# code above, created a variable high_stat_count that will raise the counter by 1 each time.. 
# it finds a stat value greater than or equal to 13 


total = 0
for stat in nash_stats:
    total += nash_stats[stat]
print (total)    

# the code above creates a variable named total and sets it equal to zero. For loop goes through 
# the dictionary individually and adds the stat value to the total 

