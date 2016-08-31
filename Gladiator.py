import random
import sys


class Gladiator:
    def __init__(self, name, health, rage, high_damage, low_damage):
        self.name = name
        self.health = health
        self.rage = rage
        self.high_damage = high_damage
        self.low_damage = low_damage

    def slash(self, other):
        """ Gladiator -> Gladiator

        Takes in two Gladiators as parameters. Self is calling attack on other.
        Other's health is lowered by a random integer within the range of low_damage and high_damage stats of self.
        Self's rage is increased by fifteen unless a randomly chosen number is greater than self's current rage. If
        This random number is chosen the number subtracted from other's health is doubled and self's rage is changed to zero.

        Glad1 health is 100 and rage is 0
        Glad2 health is 100 and rage is 0

        Glad1.slash(Glad2)

        Glad1 health is 100 and rage is 15
        Glad2 health is 85 and rage is 0
         """
        hits = random.randint(self.low_damage, self.high_damage)
        randrage = random.randint(0, 100)
        if self.rage >= randrage:
            hits *= 2
            self.rage = 0
        else:
            self.rage += 15

        other.health -= hits


    def taunt(self, other):
        """
        Gladiator -> Gladiator


        Self calls taunt on other. If other's rage is equal to or below 9 taunt does not take effect.
        If taunt does take effect, a randon number is chosen and self's rage is increased by this number while
        other's is reduced by this number.

        example:
        glad1 rage is 20
        glad2 is 50.
        gald1.taunt(glad2)

        glad1 rage is now 30
        glad2 rage is now 40
        """
        if other.rage <= 9:
            print('taunt has no effect')
        else:
            num = random.randint(0, 10)
            other.rage -= num
            self.rage += num


    def sling(self, other):
        """
        Gladiator -> Gladiator

        Self attacks other.
        Other's health is lowered by a random number in the range of zero and twenty.

        example:
        glad1 health = 100
        glad2 health = 100

        glad1.sling(glad2)

        glad1 health = 100
        glad2 health = 100
        """
        num = random.randint(0, 20)
        other.health -= num


    def stab(self, other):
        """
        Gladiator -> Gladiator

        Self attacks Other.
        A random number is chosen between the range of zero and twenty-five.
        If the number is greater than twenty-three then other's health is decreased by 10.
        If the number is less than twenty-five and greater than five, other's health is decreased by the random number.
        If the number does not meet any of the previous criteria then 'stab misses' is printed and other's health is not
        effected.
        """
        num = random.randint(0, 25)
        if num > 23:
            other.health -= 30
        elif num < 25 and num > 5:
            other.health -= num
        else:
            print('stab misses')


    def heal(self):
        """Takes in a Gladiator as a parameter.
        Players health is increased by one if their rage is also less than or equal to nine.
        If the players rage is ten or higher, their rage is lowered by ten and thier health
        is increased by 5.
        """
        if self.rage <= 9:
            self.health += 1
            print('WARNING LOWER RAGE DECREASES HEALING')
            print(self.name, 'heals 1 point')

        else:
            self.health += 5
            self.rage -= 10
            return True
        return None


    def is_dead(self):
        """
        (Gladiator) -> Boolean

        Returns if a player is dead or not.
        A player is dead if their health is below zero.
        """
        if self.health < 1:
         print(self.name ,' is dead')
         sys.exit()


    def turn(player, other):
        """ (Gladiator) -> Player choice
        Determines what a turn is and accepts input for what the palyer wants to do
        during his turn."""

        print('What will', player.name, 'do? ')
        choice = input().strip().upper()
        if choice == "S":
            player.slash(other)
        elif choice == 'H':
            player.heal()
        elif choice == "B":
            player.stab(other)
        elif choice == "T":
            player.taunt(other)
        elif choice == "C":
            player.sling(other)
        elif choice == 'QQ':
            print('ARE YOU NOT ENTERTAINED?!?!?!?')
            print(player.name, " is dead")
            sys.exit()
        else:
            print(choice)
            print('invalid input, turn lost')

    def __str__(self):
        """
        Prints out player's character's current health and rage
        """
        return self.name + " has HP of " + str(
            self.health) + " and has rage of " + str(self.rage)
