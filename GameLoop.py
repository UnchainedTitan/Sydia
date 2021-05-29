import os
from os import system
import main
import random
import time
import pickle


os.system("cls")

level_up = 100



def lesser_potion():
    if main.pyropoison.pots >= 1:
        main.pyropoison.health += 50
        main.pyropoison.pots -= 1
        print("You gain 50 health")
        health_check()
        print(f"You now have {main.pyropoison.health} ")
    else:
        print("You don't have enough potions.")

def health_potion():
    if main.pyropoison.health_pot >= 1:
        main.pyropoison.health += 150
        main.pyropoison.health_pot -= 1
        print("You gain 150 health")
        health_check()
        print(f"You now have {main.pyropoison.health} ")
    else:
        print("You don't have enough potions.")

def health_check():
    if main.pyropoison.health > main.pyropoison.max_health:
        main.pyropoison.health = main.pyropoison.max_health
    else:
        pass

def Level_Up():
    if main.pyropoison.exp >= main.pyropoison.level_up:
        main.pyropoison.level += 1
        main.pyropoison.exp = main.pyropoison.exp - main.pyropoison.level_up
        main.pyropoison.level_up += 125
        main.pyropoison.str += random.randint(1, 5)
        main.pyropoison.max_health += random.randint(10, 20)
        main.pyropoison.dex += random.randint(1, 5)
        main.pyropoison.intel += random.randint(1, 5)
        main.pyropoison.health = main.pyropoison.max_health
        print("")
        print("")
        print("You leveled Up!")
    else:
        pass

def menu():

    print("")
    print(".:#################################:.")
    print(".:#################################:.")
    print(".:#Type 'battle' to fight an enemy:.")
    print(".:#Type 'me' to view your stats ##:.")
    print(".:#Type 'inv' to view inventory ##:.")
    print(".:##Type 'pot' to use a potion ###:.")
    print(".:##type 'health pot' to use lesser potion##:.")
    print(".:##Type 'Shop' to buy things  ###:.")
    print(".:##Type 'quit' to exit the game#.:.")
    print(".:Type Save to save or load to load:.")
    print(".:#################################:.")
    print(".:#################################:.")

menu()





def equip0():

        if "Light Shirt" in main.player_inv:
            main.pyropoison.str += main.light_shirt.str
            print(f"You gained: {main.light_shirt.max_health} Maximum health ")
            print(f"{main.light_shirt.dex} Dex and {main.light_shirt.intel} intel")
            main.pyropoison.max_health += main.light_shirt.max_health
            main.pyropoison.intel += main.light_shirt.intel
            main.pyropoison.dex += main.light_shirt.dex
            main.player_inv.remove("Light Shirt")
            main.player_Eqpt.add("Light Shirt")
            time.sleep(1)
            print("")
            eqpt()
        else:
            menu()

def equip1():
    if "Crude Club" in main.player_inv:
        main.pyropoison.str += main.crude_club.str
        main.pyropoison.max_health += main.crude_club.max_health
        main.pyropoison.intel += main.crude_club.intel
        main.pyropoison.dex += main.crude_club.dex
        print(f"You gained: {main.crude_club.str} strength,  {main.crude_club.max_health} Maximum health ")
        print(f"{main.crude_club.dex} Dex and {main.crude_club.intel} intel")
        main.player_inv.remove("Crude Club")
        main.player_Eqpt.add("Crude Club")
        time.sleep(1)
        print("")
        eqpt()
    else:
        menu()

def eqpt():
    print(f"Your Equipment: {main.player_Eqpt}")
    print("Type name of the item you would like to equip.")
    player_choice = input("Item Name -> ")



    if player_choice == "light shirt":
        equip0()
        time.sleep(1)

    elif player_choice == "crude club":
        equip1()
        time.sleep(1)

    elif player_choice == "back":
        menu()


    else:
        print("Please type a valid command.")
        menu()



def inventory():
    print("Your inventory:")
    time.sleep(.5)
    print(f"Lesser potions: {main.pyropoison.pots}")
    print(f"Health potions: {main.pyropoison.health_pot}")
    print(f"Gold: {main.pyropoison.gold}")
    print(f"Your Inventory: {main.player_inv}")
    eqpt()





def battle_thug():
    main.fighting = main.bad_guy.id
    print(f"A {main.bad_guy.name} walks up to you, he looks like he is ready for a fight.")
    print(f"Type 'attack' to attack the {main.bad_guy.name}.")
    time.sleep(1)
    print("Type 'pot' to use a potion, type 'health pot' to use a bigger potion.")
    print("Type 'slam' to use your ability.")
    turn_count = 0
    while turn_count <= 10:
        player_choice = input("-> ")
        if main.bad_guy.health >= 0 and player_choice == "attack":
            main.pyropoison.player_attack()
            time.sleep(1)
            print("")
            main.got_hit()

        elif main.bad_guy.health >= 0 and player_choice == "slam" and main.pyropoison.stamina >= 15:
            main.pyropoison.player_slam()
            time.sleep(1)
            print("")
            main.got_hit()


        elif player_choice == "pot":
            lesser_potion()

        elif player_choice == "health pot":
            health_potion()



        elif main.bad_guy.health <= 0 or main.pyropoison.health <= 0:
            print("#############")
            print(" Battle over")
            print("#############")

            if main.pyropoison.health <= 0:
                time.sleep(1.3)
                print("#############")
                print("  You Lose!")
                print("#############")
                time.sleep(1.3)
                main.pyropoison.health = 50
                main.pyropoison.pots += 1
                menu()
                main.bad_guy = main.enemy(random.randint(100, 110), 15, 18, 17, "Thug", 0)

            elif main.bad_guy.health <= 0:


                time.sleep(1.3)
                print("#############")
                print("  You win!")
                print(" You find 25g")
                print("You gain 25 exp")
                print("#############")


                time.sleep(1.3)
                main.pyropoison.gold += 25
                main.pyropoison.exp += 25
                menu()
                main.bad_guy = main.enemy(random.randint(100, 110), 15, 18, 17, "Thug", 0)
                level_up = 100
                Level_Up()


            break


def battle_ugly_dude():
    print(f"An {main.ugly_dude.name} walks up to you, he points a shaky finger in your direction and declares you his enemy.")
    print(f"Type 'attack' to attack the {main.ugly_dude.name}.")
    time.sleep(1)
    print("Type 'pot' to use a potion, type 'health pot' to use a bigger potion.")
    print("Type 'slam' to use your ability.")
    turn_count = 0
    main.fighting = main.ugly_dude.id
    level_up = 100
    while turn_count <= 10:
        player_choice = input("-> ")
        if main.ugly_dude.health >= 0 and player_choice == "attack":
            main.pyropoison.player_attack()
            time.sleep(1)
            print("")
            main.got_hit()

        elif main.ugly_dude.health >= 0 and player_choice == "slam" and main.pyropoison.stamina >= 15:
            main.pyropoison.player_slam()
            time.sleep(1)
            print("")
            main.got_hit()


        elif player_choice == "pot":
            lesser_potion()

        elif player_choice == "health pot":
            health_potion()



        elif player_choice == "pot":
            lesser_potion()

        elif player_choice == "health pot":
            health_potion()


        elif main.ugly_dude.health <= 0 or main.pyropoison.health <= 0:
            print("#############")
            print(" Battle over")
            print("#############")

            if main.pyropoison.health <= 0:
                time.sleep(1.3)
                print("#############")
                print("  You Lose!")
                print("#############")
                time.sleep(1.3)
                main.pyropoison.health = 50
                main.pyropoison.pots += 1
                menu()
                main.ugly_dude = main.enemy(random.randint(120, 160), 22, 4, 15, "Ugly Looking dude", 1 )

            elif main.ugly_dude.health <= 0:
                time.sleep(1.3)
                print("###############")
                print("  You win!")
                print(" You find 40g")
                print("You gain 50 exp")
                print("###############")
                time.sleep(1.3)
                main.pyropoison.gold += 40
                main.pyropoison.exp += 50
                menu()
                main.ugly_dude = main.enemy(random.randint(120, 160), 22, 4, 15, "Ugly Looking dude", 1 )
                Level_Up()

            break

def battle_boss_thug():
    print(f"A {main.boss_thug.name} walks up to you, he slams his fists into his chest and grunts. 'Your Ass is grass'")
    print(f"Type 'attack' to attack the {main.boss_thug.name}.")
    time.sleep(1)
    print("Type 'pot' to use a potion, type 'health pot' to use a bigger potion.")
    print("Type 'slam' to use your ability.")
    turn_count = 0
    main.fighting = main.boss_thug.id
    level_up = 100
    while turn_count <= 10:
        player_choice = input("-> ")
        if main.boss_thug.health >= 0 and player_choice == "attack":
            main.pyropoison.player_attack()
            time.sleep(1)
            print("")
            main.got_hit_boss()

        elif main.boss_thug.health >= 0 and player_choice == "slam" and main.pyropoison.stamina >= 15:
            main.pyropoison.player_slam()
            time.sleep(1)
            print("")
            main.got_hit_boss()


        elif player_choice == "pot":
            lesser_potion()

        elif player_choice == "health pot":
            health_potion()

        elif player_choice == "pot":
            lesser_potion()

        elif player_choice == "health pot":
            health_potion()
        elif player_choice == "reset":
            main.boss_thug.health = 200

        elif main.boss_thug.health <= 0 or main.pyropoison.health <= 0:
            print("#############")
            print(" Battle over")
            print("#############")

            if main.pyropoison.health <= 0:
                time.sleep(1.3)
                print("#############")
                print("  You Lose!")
                print("#############")
                time.sleep(1.3)
                main.pyropoison.health = 50
                main.pyropoison.pots += 1
                menu()
                main.boss_thug = main.enemy(random.randint(170, 200), 35, 10, 29, "Boss Thug", 2)

            elif main.boss_thug.health <= 0:
                time.sleep(1.3)
                print("###############")
                print("  You win!")
                print(" You find 200g")
                print("You gain 200 exp")
                print("###############")
                time.sleep(1.3)
                main.pyropoison.gold += 200
                main.pyropoison.exp += 150
                menu()
                main.boss_thug = main.enemy(random.randint(170, 200), 35, 10, 29, "Boss Thug", 2)
                Level_Up()

            break

def battle_dire_wolf():
    print(f"A {main.dire_wolf.name} walks up to you and Snarls.")
    print(f"Type 'attack' to attack the {main.dire_wolf.name}.")
    time.sleep(1)
    print("Type 'pot' to use a potion, type 'health pot' to use a bigger potion.")
    print("Type 'slam' to use your ability.")
    turn_count = 0
    main.fighting = main.dire_wolf.id
    level_up = 100
    while turn_count <= 10:
        player_choice = input("-> ")
        if main.dire_wolf.health >= 0 and player_choice == "attack":
            main.pyropoison.player_attack()
            time.sleep(1)
            print("")
            main.got_hit()

        elif main.dire_wolf.health >= 0 and player_choice == "slam" and main.pyropoison.stamina >= 15:
            main.pyropoison.player_slam()
            time.sleep(1)
            print("")
            main.got_hit()


        elif player_choice == "pot":
            lesser_potion()

        elif player_choice == "health pot":
            health_potion()

        elif player_choice == "pot":
            lesser_potion()

        elif player_choice == "health pot":
            health_potion()




        elif main.dire_wolf.health <= 0 or main.pyropoison.health <= 0:
            print("#############")
            print(" Battle over")
            print("#############")

            if main.pyropoison.health <= 0:
                time.sleep(1.3)
                print("#############")
                print("  You Lose!")
                print("#############")
                time.sleep(1.3)
                main.pyropoison.health = 50
                main.pyropoison.pots += 1
                menu()
                main.dire_wolf = main.enemy(random.randint(185, 190), 28, 5, 25, "Dire Wolf", 3)

            elif main.dire_wolf.health <= 0:
                time.sleep(1.3)
                print("###############")
                print("  You win!")
                print(" You find 75g")
                print("You gain 100 exp")
                print("###############")
                time.sleep(1.3)
                main.pyropoison.gold += 75
                main.pyropoison.exp += 100
                menu()
                main.dire_wolf = main.enemy(random.randint(185, 190), 28, 5, 25, "Dire Wolf", 3)
                Level_Up()

            break


def player_stats():

    print("Your Stats:")
    print(f"Name: {main.pyropoison.name} ")
    print(f"Health: {main.pyropoison.health}" + f"/{main.pyropoison.max_health}")
    time.sleep(1.2)
    print(f"Strength: {main.pyropoison.str}")
    time.sleep(1.2)
    print(f"Intellect: {main.pyropoison.intel}")
    time.sleep(1.2)
    print(f"Dexterity: {main.pyropoison.dex}")
    time.sleep(1.2)
    print(f"Level: {main.pyropoison.level}")
    time.sleep(1.2)
    print(f"Exp: {main.pyropoison.exp}")
    time.sleep(1.2)
    print(f"EXP to next level: {main.pyropoison.level_up}")



running = True
while running == True:
    player_choice = input("-> ")



    if player_choice == "battle":
        print("Avalible enemies: 'thug', 'ugly', 'dire wolf' and  'boss thug'")
        enemy = input("Who would you like to battle? ")
        if enemy == "thug":
            battle_thug()
        if enemy == "ugly":
            battle_ugly_dude()
        if enemy == "boss thug":
            battle_boss_thug()
        if enemy == "dire wolf":
            battle_dire_wolf()
        else:
            pass

    elif player_choice == "me":
        player_stats()
        time.sleep(1)
        menu()

    elif player_choice == "inv":
        inventory()
        time.sleep(1)



    elif player_choice == "pot":
        if main.pyropoison.pots >= 1:
            main.pyropoison.health += 50
            main.pyropoison.pots -= 1
            print("You gain 50 health")
            health_check()
            print(f"You now have {main.pyropoison.health} ")
        else:
            print("You don't have enough potions.")

    elif player_choice == "health pot":
        if main.pyropoison.health_pot >= 1:
            main.pyropoison.health += 150
            main.pyropoison.health_pot -= 1
            print("You gain 150 health")
            health_check()
            print(f"You now have {main.pyropoison.health} ")
        else:
            print("You don't have enough potions.")



    elif player_choice == "shop":
        time.sleep(1.3)
        print("A gray haired lady examines you over her round eye glasses. She rolls her eyes and sighs")
        print("All we have right now are potions, maybe in the future I can offer you more.")
        print(f"Your Gold: {main.pyropoison.gold}")
        time.sleep(0.5)
        print("Lesser potion: 50g")
        print("Health potion: 125g")
        print("Type 'lesser potion' or 'health potion' to buy a potion.")
        player_choice = input("-> ")

        if player_choice == "no":
            print("Maybe next time.")
            print("The shop keep waves you out the door.")
            time.sleep(1.2)
            menu()

        elif main.pyropoison.gold >= 50 and player_choice == "lesser potion":
            main.pyropoison.gold -= 50
            main.pyropoison.pots += 1
            print("The Lady hands you the lesser potion and takes your gold. ")
            print("'Thank you' she says.")
            print("You leave.")
            time.sleep(1.3)
            menu()

        elif main.pyropoison.gold >= 125 and player_choice == "health potion":
            main.pyropoison.gold -= 125
            main.pyropoison.health_pot += 1
            print("The Lady hands you the health potion and takes your gold. ")
            print("'Thank you' she says.")
            print("You leave.")
            time.sleep(1.3)
            menu()

        else:
            print("You don't have the gold, Leave here!")
            time.sleep(1.3)
            menu()


    elif player_choice == "quit":
        print("Thanks for playing!")
        print("Shutting down.")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        running = not True

    elif player_choice == "load":
        main.pyropoison = pickle.load(open("save.dat", "rb"))
        main.player_inv = pickle.load(open("inv.dat", "rb"))
        main.player_Eqpt = pickle.load(open("eqpt.dat", "rb"))
        time.sleep(1)
        print("You loaded your game")
    elif player_choice == "save":
        pickle.dump(main.player_inv, open("inv.dat", "wb"))
        pickle.dump(main.pyropoison, open("save.dat", "wb"))
        pickle.dump(main.player_Eqpt, open("eqpt.dat", "wb"))
        time.sleep(1)
        print("You saved the Game")


    else:
        print("Please type a Valid Command.")
        continue



