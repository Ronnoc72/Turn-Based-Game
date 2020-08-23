import random


class Player:
    def __init__(self, name, attack, health, max_health, max_attack, style):
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = max_health
        self.max_attack = max_attack
        self.style = style

    def getAttack(self):
        return self.attack

    def getMaxAttack(self):
        return self.max_attack

    def getHealth(self):
        return self.health

    def getMaxHealth(self):
        return self.max_health

    def getName(self):
        return self.name

    def getStyle(self):
        return self.style

    def upgradeAttack(self):
        self.attack += 3
        return print("You drank a strength potion!")

    def downgradeAttack(self):
        self.attack -= 3
        return print("You potion wore off!")

    def playerDeath(self):
        if self.getHealth() <= 0:
            return True


class Knight(Player):
    def setPlayer(self):
        self.style = "Knight"
        self.attack = 6
        self.health = 30
        self.max_health = 30
        self.max_attack = 6

    def healPlayer(self):
        self.health += 6
        if self.health >= self.max_health:
            self.health = 30
        return print("Player was healed!")

    def specialMove(self):
        self.health += 3
        return print("You've activated your special move, your defense increased!")

    def specialMoveReturn(self):
        self.health -= 3
        return print("Your defense wen't back to normal!")


class Mage(Player):
    def setPlayer(self):
        self.style = "Mage"
        self.attack = 8
        self.health = 25
        self.max_health = 25
        self.max_attack = 8

    def healPlayer(self):
        self.health += 7
        if self.health >= self.max_health:
            self.health = 25

    def specialMove(self):
        self.attack = 3
        return print("You've activated your special move, your next attack will hit everyone!")

    def specialMoveReturn(self):
        self.attack = 8


class Archer(Player):
    def setPlayer(self):
        self.style = "Archer"
        self.attack = 7
        self.health = 28
        self.max_health = 28
        self.max_attack = 7

    def healPlayer(self):
        self.health += 6
        if self.health >= self.max_health:
            self.health = 28

    def specialMove(self):
        self.attack += 5
        return print("You've activated your special move, your next attack is a one shot kill!")

    def specialMoveReturn(self):
        self.attack -= 5


class Healer(Player):
    def setPlayer(self):
        self.style = "Healer"
        self.attack = 5
        self.health = 34
        self.max_health = 34
        self.max_attack = 5

    def healPlayer(self):
        self.health += 8
        if self.health >= self.max_health:
            self.health = 34

    def specialMove(self):
        self.health += 10
        return print("You've activated your special move, you've healed 10 health points!")

    def specialMoveReturn(self):
        self.health += 0


class Enemy:
    def __int__(self, enemy_name, enemy_attack, enemy_health, enemy_max_health):
        self.enemy_name = enemy_name
        self.enemy_attack = enemy_attack
        self.enemy_health = enemy_health
        self.enemy_max_health = enemy_max_health

    def getName(self):
        return self.enemy_name

    def enemyAttack(self):
        return self.enemy_attack

    def enemyHealth(self):
        return self.enemy_health

    def enemyMaxHealth(self):
        return self.enemy_max_health

    def isDead(self):
        if self.enemyHealth() <= 0:
            return True

    def dropPotion(self):
        if self.enemyHealth() <= 0:
            if random.randint(1, 3) == 1:
                return True


class Goblin(Enemy):
    def __init__(self):
        self.enemy_attack = 0
        self.enemy_health = 0
        self.enemy_max_health = 5
        self.enemy_name = "Goblin"

    def healEnemy(self):
        self.enemy_health += 1
        if self.enemy_health >= self.enemy_max_health:
            self.enemy_health = 5
        return print("The Goblin Healed!")

    def findHealth(self):
        self.enemy_health = random.randint(3, 5)
        self.enemy_max_health = self.enemy_health

    def findAttack(self):
        self.enemy_attack = random.randint(1, 2)

    @staticmethod
    def encounter():
        return print("You encountered a Goblin!")

    @staticmethod
    def hurt():
        num = random.randint(1, 3)
        if num == 1:
            return print("The Goblin is badly hurt")
        if num == 2:
            return print("The Goblin's leg is missing")
        if num == 3:
            return print("The Goblin is bleeding")


class SuperGoblin(Enemy):
    def __init__(self):
        self.enemy_name = "Super Goblin"
        self.enemy_attack = 0
        self.enemy_max_health = 0
        self.enemy_health = 0

    def findHealth(self):
        self.enemy_health = round(random.randint(6, 9))
        self.enemy_max_health = self.enemy_health

    def findAttack(self):
        self.enemy_attack = random.randint(4, 5)

    def healEnemy(self):
        if self.enemy_health < self.enemy_max_health:
            self.enemy_health += 1
            if self.enemy_health >= self.enemy_max_health:
                self.enemy_health = self.enemy_max_health
        return print("The Super Goblin Healed!")

    @staticmethod
    def encounter():
        return print("You encountered a Super Goblin!")

    @staticmethod
    def hurt():
        num = random.randint(1, 3)
        if num == 1:
            return print("The Super Goblin is badly hurt")
        if num == 2:
            return print("The Super Goblin's arm is broken")
        if num == 3:
            return print("The Super Goblin is bruised")


class Sorcerer(Enemy):
    def __init__(self):
        self.enemy_attack = 0
        self.enemy_max_health = 4
        self.enemy_health = 4
        self.enemy_name = "Sorcerer"

    def healEnemy(self):
        self.enemy_health += 1
        if self.enemy_health >= self.enemy_max_health:
            self.enemy_health = 4
        return print("The Sorcerer Healed!")

    def findHealth(self):
        self.enemy_health = random.randint(3, 5)
        self.enemy_max_health = self.enemy_health

    def findAttack(self):
        self.enemy_attack = random.randint(5, 7)

    @staticmethod
    def encounter():
        return print("You encountered a Sorcerer!")

    @staticmethod
    def hurt():
        num = random.randint(1, 3)
        if num == 1:
            return print("The Sorcerer's staff paint is chipping")
        if num == 2:
            return print("The Sorcerer's robe is torn")
        if num == 3:
            return print("The Sorcerer has cuts on their face")
