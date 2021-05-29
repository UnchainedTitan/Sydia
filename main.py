import random
import pickle
import time



fighting = int

# This is the enemy class
class enemy:
    def __init__(self, health, str, intel, dex, name, id):

        self.health = health
        self.str = str
        self.intel = intel
        self.dex = dex
        self.name = name
        self.id = id


# This is the player class
class Player:
    def __init__(self, health, str, intel, dex, pots, gold, level, exp,level_up, max_health, name, health_pot, stamina):

        self.health = health
        self.str = str
        self.intel = intel
        self.dex = dex
        self.pots = pots
        self.gold = gold
        self.level = level
        self.exp = exp
        self.level_up = level_up
        self.max_health = max_health
        self.name = name
        self.health_pot = health_pot
        self.stamina = stamina

    # This is the Hit method of the player
    def player_attack(self):

        # Chooses the enemy based on what ID is being used.


        global Enemy

        if fighting == 1:
            Enemy = ugly_dude
            ugly_dude.health = Enemy.health
        elif fighting == 0:
            Enemy = bad_guy
            bad_guy.health = Enemy.health
        elif fighting == 2:
            Enemy = boss_thug
            boss_thug.health = Enemy.health
        elif fighting == 3:
            Enemy = dire_wolf
            dire_wolf.health = Enemy.health

        pyropoison.stamina += 5
        damage = random.uniform(10+pyropoison.str, 20+pyropoison.str) + self.str
        hit_mod = self.dex * 0.7
        attack_value = random.uniform(10, 30 + (pyropoison.dex/2)) + hit_mod

        if attack_value > Enemy.dex:
            print(f"You hit {Enemy.name} for {damage}.")
            Enemy.health -= damage
            print(f"{Enemy.name} has {Enemy.health} life left")
            print(f"Your Stamina: {pyropoison.stamina}")


        else:
            print("############")
            print("You missed!")
            print("############")
        return Enemy.health


    def player_slam(self):
        global Enemy

        if fighting == 1:
            Enemy = ugly_dude
            ugly_dude.health = Enemy.health
        elif fighting == 0:
            Enemy = bad_guy
            bad_guy.health = Enemy.health
        elif fighting == 2:
            Enemy = boss_thug
            boss_thug.health = Enemy.health
        elif fighting == 3:
            Enemy = dire_wolf
            dire_wolf.health = Enemy.health

        damage = random.uniform(18 + pyropoison.str, 20 + pyropoison.str) + (self.str * 2)
        hit_mod = self.dex * 0.7
        attack_value = random.uniform(18, 30 + (pyropoison.dex / 2)) + hit_mod
        pyropoison.stamina -= 15
        if attack_value > Enemy.dex:
            print(f"You slam {Enemy.name} bludgeoning his body for {damage}.")
            Enemy.health -= damage
            print(f"{Enemy.name} has {Enemy.health} life left")
            print(f"You used 15 stamina, you have {pyropoison.stamina} left.")



        else:
            print("############")
            print("You missed!")
            print("############")
        return Enemy.health





# This is the item class
class item:
    def __init__(self,str,intel,dex,max_health, name, value, id):

        self.str = str
        self.intel = intel
        self.dex = dex
        self.max_health = max_health
        self.name = name
        self.value = value
        self.id = id



#  health, str, intel, dex, name, id
pyropoison = Player(random.randint(100, 110), 20, 20,20, 1, 100, 1, 0, 100, 110, "", 1, 50 )
bad_guy = enemy(random.randint(100, 110), 15, 18, 17, "Thug", 0 )
ugly_dude = enemy(random.randint(120, 160), 22, 4, 15, "Ugly Looking dude", 1 )
boss_thug = enemy(random.randint(170,200),35,10,29,"Boss thug", 2)
dire_wolf = enemy(random.randint(185, 190), 28, 5, 25, "Dire Wolf", 3)

crude_club = item(5,0,1,10, "Crude Club", 50,0)
light_shirt = item(0,2,4,2,"Light Shirt", 50,1)


player_inv = {
    "Light Shirt",
    "Crude Club",

}
player_Eqpt = {
    "",
    "",

}




start_count = 1
while start_count == 1:
    start = input("Would you like to load your game? ")
    start_count = 1
    if start == "no":
        pyropoison.name = input("Name Your Hero: ")
        print(f"Welcome to the pre-alpha stage of this game, {pyropoison.name}, this is a very early stage, please be aware that there may be bugs or other things that might not work 100%")
        print("Thank you for playing and have a wonderful time! Also, Don't forget to load your game if you already have a saved character!")
        print("Please remember that all commands should be typed without caps.")
        start_count -= 1
    elif start == "yes":
        pyropoison = pickle.load(open("save.dat", "rb"))
        player_inv = pickle.load(open("inv.dat", "rb"))
        player_Eqpt = pickle.load(open("eqpt.dat", "rb"))
        time.sleep(1)
        start_count -= 1
        print("You loaded your game.")
    else:
        print("Please type 'yes' or 'no'.")
        continue





#This is the getting hit function of the Player
def got_hit():

        damage = random.randint(10, 20)+ Enemy.str
        hit_mod = pyropoison.dex * 0.7
        attack_value = random.randint(10, 30) +hit_mod

        if pyropoison.dex < attack_value:

            print(f"You got hit for: {damage}")
            pyropoison.health -= damage
            print(f"You have {pyropoison.health} life left.")
        else:
            print("######################")
            print("You dodged the attack!")
            print("######################")

        return pyropoison.health


def got_hit_boss():
    damage = random.randint(30, 35) + boss_thug.str
    hit_mod = pyropoison.dex * 0.7
    attack_value = random.randint(15, 30) + hit_mod

    if pyropoison.dex < attack_value:

        print(f"The Boss Thug launches forward, wrapping his giant fingers around your entire face, he slams your skull into the ground over and over. He deals {damage} damage")
        pyropoison.health -= damage
        print(f"You have {pyropoison.health} life left.")
    else:
        print("######################")
        print("You dodged the attack!")
        print("######################")

    return pyropoison.health






