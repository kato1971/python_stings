# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

""" PART 1 """
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)

report = scorer_0 + " " + "scored in the" + " " + str(goal_0) + "nd minute" + "\n" + scorer_1 + " " + "scored in the" + " " + str(goal_1) + "th minute"

""" PART 2 """
player = "Frank Rijkaard"

find_first_name = player.find("Frank")
first_name = player[:5]
print(first_name)

find_last_name = player.find("Rijkaard")
last_name_len = len(player[6:])
print(last_name_len)

name_short = player.replace("Frank", "F.")
print(name_short)

first_name_len = len(player[:5])
chant_1 = (first_name + "!" + " ") * first_name_len
chant = chant_1[:-1]
print(chant)

good_chant =  chant != 3
print(good_chant)
print(chant != 2)
