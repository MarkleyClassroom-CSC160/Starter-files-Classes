# fighters_lists.py -- Step 1 of the lecture: why objects?
# Two fighters stored the way we've stored things so far: lists.

hero = ["Aria", 30, 8]
goblin = ["Grub the Goblin", 25, 8]

print(hero[0], "has", hero[1], "HP")
print(goblin[0], "has", goblin[1], "HP")

# the hero hits the goblin
goblin[1] = goblin[1] - hero[2]
print(goblin[0], "has", goblin[1], "HP")
