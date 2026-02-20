print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
side = str(input("left or right? "))
if side == "left":
    print("You've come to a lake. There is an island in the middle of the lake. ")
    print("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    swim_or_wait = str(input("swim or wait? "))
    if swim_or_wait == "wait":
        print ("You  arrive at the island unharmed.There is a housewith 3 doors.")
        door = input("Which door? red, blue or yellow? ")
        if door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif door == "yellow":
            print("YOU WIN!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")