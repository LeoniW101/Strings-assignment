# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

#1.1  Add your code after this line
#every player that scored
scoringplayer1 = 'Ruud Gullit'
scoringplayer2 = 'Marco van Basten'

#1.2 each minute of match that goal was scored
goal_0 = 32
goal_1 = 54

# 1.3 Using + create string that reports who scored when
scorers = scoringplayer1 + " " + str(goal_0)+","" "+ scoringplayer2+ " "+str(goal_1)

#1.4 f string
report = f"{scoringplayer1} scored in the {goal_0}nd minute\n{scoringplayer2} scored in the {goal_1}th minute"

#Part 2
#2.1
player = 'Ruud Gullit'
#2.2
first_name = player[:player.find(' ')][0:]

#2.3
last_name_len = len(player[player.find(" "):] [:-1])
#2.4
last_name = player[player.find(" "):] [1:]

name_short = first_name[0:1] + '. ' + last_name

#2.5
chant_full = f"{first_name}! " * int(len(first_name))
chant=chant_full[:-1]

#2.6
good_chant = chant[-1] != ' '