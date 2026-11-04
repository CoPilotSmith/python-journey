# John Stockton my boy, dropping dimes! No Mailman until Day 32 though 

stockton_stats = {
    "points" : 154,
    "assists" : 15,
    "jersey_number" : 12
}
print (stockton_stats)

for stat in stockton_stats:
    print (stat,stockton_stats[stat])

# the above code will return a print statement that prints the "stat" which are 
# points, assists, and jersey number. the "stockton_stats[stat]" is printing the value associated with that 
# stat, ie --> jersey number would be 12, points would be 154


for stat in stockton_stats:
    if stockton_stats[stat] > 12:
        print (stat, stockton_stats[stat])

# the script above is running a for loop, checking the stats in the dictionary stockton_stats
# if the stat value is greater than 12, then it will print the stat and the value tied with it 



