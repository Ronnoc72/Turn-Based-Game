import re
import random
from TBG_CLASS import *

character_selection_pattern = r"[!@#$%^&*()]"
running = False
running2 = False
running3 = False
running4 = False
running5 = False
running6 = False
running7 = False
i = 0
j = 0
x = 0
timer = 0
dead = 0
drinks = 0
inventory = []
enemy_list = []
enemy_list_objects = []
enemy_list_health = []

need_help = input("Do you need to see the help menu? : ")
if need_help == "yes" or need_help == "YES" or need_help == "Yes":
    f = open("TBG_HELP.txt", "r")
    print(f.read())

startingName = input("Enter a name for your player: ")
current_player = ""
print("Select your hero!  Knight(1)  Mage(2)  Archer(3)  Healer(4)")
character_selection = input("")

if re.search(character_selection_pattern, character_selection) or character_selection == "":
    print("Invalid Character Choice, Restart")
    raise Exception("Restart")

if character_selection == "1" or character_selection == "Knight" or character_selection == "knight":
    knight = Knight(startingName, 0, 0, 0, 0, '')
    knight.setPlayer()
    current_player = knight

if character_selection == "2" or character_selection == "Mage" or character_selection == "mage":
    mage = Mage(startingName, 0, 0, 0, 0, '')
    mage.setPlayer()
    current_player = mage

if character_selection == "3" or character_selection == "Archer" or character_selection == "archer":
    archer = Archer(startingName, 0, 0, 0, 0, '')
    archer.setPlayer()
    current_player = archer

if character_selection == "4" or character_selection == "Healer" or character_selection == "healer":
    healer = Healer(startingName, 0, 0, 0, 0, '')
    healer.setPlayer()
    current_player = healer

running = True
while running:
    for i in range(round(random.randint(3, 5))):
        finding_enemies = random.randint(1, 5)
        if finding_enemies == 1 or finding_enemies == 2 or finding_enemies == 3:
            goblin = Goblin()
            goblin.findHealth()
            goblin.findAttack()
            goblin.encounter()
            enemy_list.append(goblin.getName())
            enemy_list_health.append(goblin.enemyHealth())
            enemy_list_objects.append(goblin)
        elif finding_enemies == 4:
            super_goblin = SuperGoblin()
            super_goblin.findHealth()
            super_goblin.findAttack()
            super_goblin.encounter()
            enemy_list.append(super_goblin.getName())
            enemy_list_health.append(super_goblin.enemyHealth())
            enemy_list_objects.append(super_goblin)
        elif finding_enemies == 5:
            sorcerer = Sorcerer()
            sorcerer.findHealth()
            sorcerer.findAttack()
            sorcerer.encounter()
            enemy_list.append(sorcerer.getName())
            enemy_list_health.append(sorcerer.enemyHealth())
            enemy_list_objects.append(sorcerer)
        i += 1
    running = False

    running1 = True
    while running1:
        if not enemy_list:
            i = 0
            running = True
            break
        print("\n")
        print("What is your action?")
        action = input("")
        running1 = False
        if action == "e" or action == "E":
            running2 = True
        if action == "a" or action == "A":
            running3 = True
        if action == "s" or action == "S":
            running6 = True
        while running2:
            print(inventory)
            selection = input("")
            running2 = False
            if selection == "" or selection == " ":
                running1 = True
            elif selection == "1":
                if inventory[0] == "health potion":
                    current_player.healPlayer()
                    inventory.pop(0)
                    drinks += 1
                    running1 = True
                elif inventory[0] == "strength potion":
                    current_player.upgradeAttack()
                    timer = 0
                    inventory.pop(0)
                    drinks += 1
                    running1 = True
            elif selection == "2":
                if inventory[1] == "health potion":
                    current_player.healPlayer()
                    inventory.pop(1)
                    drinks += 1
                    running1 = True
                elif inventory[1] == "strength potion":
                    current_player.upgradeAttack()
                    timer = 0
                    inventory.pop(1)
                    drinks += 1
                    running1 = True
            elif selection == "3":
                if inventory[2] == "health potion":
                    current_player.healPlayer()
                    inventory.pop(2)
                    drinks += 1
                    running1 = True
                elif inventory[2] == "strength potion":
                    current_player.upgradeAttack()
                    timer = 0
                    inventory.pop(2)
                    drinks += 1
                    running1 = True
        while running3:
            print("\n")
            print(enemy_list)
            print(enemy_list_health)
            selection = input("")
            running3 = False
            if selection == "" or selection == " ":
                running1 = True
            elif selection == "1" and len(enemy_list_objects) >= 1:
                enemy_list_objects[0].enemy_health -= current_player.getAttack()
                enemy_list_objects[0].hurt()
                j = 0
                if current_player.max_attack < current_player.attack:
                    timer += 1
                if timer == 3:
                    current_player.downgradeAttack()
                    timer = 0
                running4 = True
            elif selection == "2" and len(enemy_list_objects) >= 2:
                enemy_list_objects[1].enemy_health -= current_player.getAttack()
                enemy_list_objects[1].hurt()
                j = 1
                if current_player.max_attack < current_player.attack:
                    timer += 1
                if timer == 3:
                    current_player.downgradeAttack()
                    timer = 0
                running4 = True
            elif selection == "3" and len(enemy_list_objects) >= 3:
                enemy_list_objects[2].enemy_health -= current_player.getAttack()
                enemy_list_objects[2].hurt()
                j = 2
                if current_player.max_attack < current_player.attack:
                    timer += 1
                if timer == 3:
                    current_player.downgradeAttack()
                    timer = 0
                running4 = True
            elif selection == "4" and len(enemy_list_objects) >= 4:
                enemy_list_objects[3].enemy_health -= current_player.getAttack()
                enemy_list_objects[3].hurt()
                j = 3
                if current_player.max_attack < current_player.attack:
                    timer += 1
                if timer == 3:
                    current_player.downgradeAttack()
                    timer = 0
                running4 = True
            elif selection == "5" and len(enemy_list_objects) >= 5:
                enemy_list_objects[4].enemy_health -= current_player.getAttack()
                enemy_list_objects[4].hurt()
                j = 4
                if current_player.max_attack < current_player.attack:
                    timer += 1
                if timer == 3:
                    current_player.downgradeAttack()
                    timer = 0
                running4 = True
            else:
                running3 = True
        running4 = True
        while running4:
            enemy_list_health.pop(j)
            current_enemy = enemy_list_objects[j]
            enemy_list_health.insert(j, current_enemy.enemyHealth())
            if current_enemy.isDead():
                dead += 1
                if current_enemy.dropPotion():
                    print("The " + current_enemy.getName() + " dropped a potion")
                    if len(inventory) >= 3:
                        print("But it spilled on the ground!")
                    if len(inventory) < 3:
                        potion_random = random.randint(1, 2)
                        if potion_random == 2:
                            inventory.append("health potion")
                        if potion_random == 1:
                            inventory.append("strength potion")
                print("The " + current_enemy.getName() + " was slain")
                enemy_list_health.pop(j)
                enemy_list_objects.pop(j)
                enemy_list.pop(j)
                running5 = True
            running4 = False
        while running5:
            length = len(enemy_list_objects) - 1
            if length > 0:
                enemy_attack_random = random.randint(0, length)
                current_player.health -= enemy_list_objects[enemy_attack_random].enemyAttack()
                print(enemy_list_objects[enemy_attack_random].getName() + " attacked you for " + str(
                    enemy_list_objects[enemy_attack_random].enemyAttack()) + " damage!")
            if length == 0:
                current_player.health -= enemy_list_objects[0].enemyAttack()
                print(enemy_list_objects[0].getName() + " attacked you for " + str(
                    enemy_list_objects[0].enemyAttack()) + " damage!")
            if current_player.playerDeath():
                print("\n")
                print("GAME OVER!")
                print("You killed " + str(dead) + " enemies!")
                print("You drank " + str(drinks) + " potions")
                exit()
            running5 = False
        while running6:
            print("\n")
            print("Class: " + current_player.getStyle())
            print("Username: " + current_player.getName())
            print("Current Health: " + str(current_player.getHealth()))
            print("Max Health: " + str(current_player.getMaxHealth()))
            print("Attack: " + str(current_player.getAttack()))
            print("Max Attack: " + str(current_player.getMaxAttack()))
            running6 = False
        running1 = True
