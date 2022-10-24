from random import randint
from time import sleep


#Darlene
def pet1():
    class Darlene:
        def __init__(self, health):
            self.health = health

    class Pet(Darlene):
        def __init__(self, health = 500):
            super().__init__(health)

        def skills(self, other):
            while True:
                moves = input("\nChoose a skill to attack [1]Fade Away,[2]Hatred to All, [3]This is the End,[4]The Scent of Death: ")
                sleep(0.5)

                if moves == "1":
                    damage1 = randint(45, 65)
                    other.health -= damage1
                    print(f"\nFade Away dealt {damage1} damage".format(damage1))
                    break

                elif moves == "2":
                    damage2 = randint(60, 85)
                    other.health -= damage2
                    print(f"\nHatred to All dealt {damage2} damage".format(damage2))
                    break

                elif moves == "3":
                    damage3 = randint(55, 90)
                    other.health -= damage3
                    print(f"\nThis is the End dealt {damage3} damage".format(damage3))
                    break

                elif moves == "4":
                    damage4 = randint(100, 110)
                    other.health -= damage4
                    print(f"\nThe Scent of Death dealt {damage4}".format(damage4))
                    break

                else:
                    print("Invalid Choice")

    class Mobs(Darlene):
        def __init__(self, health = 500):
            super().__init__(health)

        def skills(self, other):
            mobDamage = randint(50, 100)
            other.health -= mobDamage
            print(f"\nThe enemy dealt {mobDamage} damage".format(mobDamage))


    def combatSystem(pet, enemy):
        mobs = randint(1, 4)
        if mobs == 1:
            mobs = "Kooii"

        if mobs == 2:
            mobs = "Recluse"

        if mobs == 3:
            mobs = "Mushroom"

        if mobs == 4:
            mobs = "Common Spider"

        print("\nPrepare for battle!")
        sleep(0.5)
        print("\nEnemy", mobs, "appears!")
        print("HP:{0.health}".format(enemy))
        print("\nPet HP:{0.health}".format(pet))
        while pet.health > 0 and enemy.health > 0:
            pet.skills(enemy)

            if enemy.health <= 0:
                break
            print("\nEnemy HP:{0.health}.".format(enemy))
            sleep(0.5)
            enemy.skills(pet)

            if pet.health <= 0:
                break
            print("\nPet HP:{0.health}.".format(pet))

        if pet.health > 0:
            print("\nYou defeated the enemy!")

        if enemy.health > 0:
            print("\nYou were defeated by the enemy!")

    if __name__ == '__main__':
        combatSystem(Pet(), Mobs())

pet1()


def pet2():
    class Barslaf:
        def __init__(self, health):
            self.health = health

    class Pet(Barslaf):
        def __init__(self, health=500):
            super().__init__(health)

        def skills(self, other):
            while True:
                moves = input("\nChoose a skill to attack [1]Absolute Zero Point,[2]Ice Spear, [3]Ice Pillar,[4]You Fools shall Die!: ")
                sleep(0.5)

                if moves == "1":
                    damage1 = randint(35, 55)
                    other.health -= damage1
                    print(f"\nAbsolute Zero Point dealt {damage1} damage".format(damage1))
                    break

                elif moves == "2":
                    damage2 = randint(40, 60)
                    other.health -= damage2
                    print(f"\nIce Spear dealt {damage2} damage".format(damage2))
                    break

                elif moves == "3":
                    damage3 = randint(50, 70)
                    other.health -= damage3
                    print(f"\nIce Pillar dealt{damage3} damage".format(damage3))
                    break

                elif moves == "4":
                    damage4 = randint(100, 110)
                    other.health -= damage4
                    print(f"\nYou Fools shall Die! dealt {damage4}".format(damage4))
                    break

                else:
                    print("Invalid Choice")

    class Mobs(Barslaf):
        def __init__(self, health=500):
            super().__init__(health)

        def skills(self, other):
            mobDamage = randint(50, 100)
            other.health -= mobDamage
            print(f"\nThe enemy dealt {mobDamage} damage".format(mobDamage))

    def combatSystem(pet, enemy):
        mobs = randint(1, 5)
        print("\nPrepare for battle!")
        sleep(0.5)
        print("\nEnemy", mobs, "appears!")
        print("HP:{0.health}".format(enemy))
        print("\nPet HP:{0.health}".format(pet))
        while pet.health > 0 and enemy.health > 0:
            pet.skills(enemy)

            if enemy.health <= 0:
                break
            print("\nEnemy HP:{0.health}.".format(enemy))
            enemy.skills(pet)

            if pet.health <= 0:
                break
            print("\nPet HP:{0.health}.".format(pet))

        if pet.health > 0:
            print("\nYou defeated the enemy!")

        if enemy.health > 0:
            print("\nYou were defeated by the enemy!")

    if __name__ == '__main__':
        combatSystem(Pet(), Mobs())


# Medusa
def pet3():
    class Medusa:
        def __init__(self, health):
            self.health = health

    class Pet(Medusa):
        def __init__(self, health=500):
            super().__init__(health)

        def skills(self, other):
            while True:
                moves = input("\nChoose a skill to attack [1]Firestorm,[2]Vortex, [3]Ravage, [4]Curse of Doom: ")
                sleep(0.5)

                if moves == "1":
                    damage1 = randint(30, 50)
                    other.health -= damage1
                    print(f"\nFirestorm dealt {damage1} damage".format(damage1))
                    break

                elif moves == "2":
                    damage2 = randint(40, 45)
                    other.health -= damage2
                    print(f"\nVortex dealt {damage2} damage".format(damage2))
                    break

                elif moves == "3":
                    damage3 = randint(50, 70)
                    other.health -= damage3
                    print(f"\nRavage dealt{damage3} damage".format(damage3))
                    break

                elif moves == "4":
                    damage4 = randint(105, 110)
                    other.health -= damage4
                    print(f"\nCurse of Doom dealt {damage4}".format(damage4))
                    break

                else:
                    print("Invalid Choice")

    class Mobs(Medusa):
        def __init__(self, health=500):
            super().__init__(health)

        def skills(self, other):
            mobDamage = randint(50, 100)
            other.health -= mobDamage
            print(f"\nThe enemy dealt {mobDamage} damage".format(mobDamage))

    def combatSystem(pet, enemy):
        mobs = randint(1, 5)
        print("\nPrepare for battle!")
        sleep(0.5)
        print("\nEnemy", mobs, "appears!")
        print("HP:{0.health}".format(enemy))
        print("\nPet HP:{0.health}".format(pet))
        while pet.health > 0 and enemy.health > 0:
            pet.skills(enemy)

            if enemy.health <= 0:
                break
            print("\nEnemy HP:{0.health}.".format(enemy))
            enemy.skills(pet)

            if pet.health <= 0:
                break
            print("\nPet HP:{0.health}.".format(pet))

        if pet.health > 0:
            print("\nYou defeated the enemy!")

        if enemy.health > 0:
            print("\nYou were defeated by the enemy!")

    if __name__ == '__main__':
        combatSystem(Pet(), Mobs())



# Ukpana
def pet4():
    class Ukpana:
        def __init__(self, health):
            self.health = health

    class Pet(Ukpana):
        def __init__(self, health=500):
            super().__init__(health)

        def skills(self, other):
            while True:
                moves = input("\nChoose a skill to attack [1]Fire of Darkness,[2]Darkness Slam, [3]Dark Pulse, [4]Power of Darkness!: ")
                sleep(0.5)

                if moves == "1":
                    damage1 = randint(35, 55)
                    other.health -= damage1
                    print(f"\nFire of Darkness dealt {damage1} damage".format(damage1))
                    break

                elif moves == "2":
                    damage2 = randint(40, 60)
                    other.health -= damage2
                    print(f"\nDarkness Slam dealt {damage2} damage".format(damage2))
                    break

                elif moves == "3":
                    damage3 = randint(50, 70)
                    other.health -= damage3
                    print(f"\nDark Pulse dealt{damage3} damage".format(damage3))
                    break

                elif moves == "4":
                    damage4 = randint(100, 110)
                    other.health -= damage4
                    print(f"\nCPower of Darkness! dealt {damage4}".format(damage4))
                    break

                else:
                    print("Invalid Choice")

    class Mobs(Ukpana):
        def __init__(self, health=500):
            super().__init__(health)

        def skills(self, other):
            mobDamage = randint(50, 100)
            other.health -= mobDamage
            print(f"\nThe enemy dealt {mobDamage} damage".format(mobDamage))

    def combatSystem(pet, enemy):
        mobs = randint(1, 5)
        print("\nPrepare for battle!")
        sleep(0.5)
        print("\nEnemy", mobs, "appears!")
        print("HP:{0.health}".format(enemy))
        print("\nPet HP:{0.health}".format(pet))
        while pet.health > 0 and enemy.health > 0:
            pet.skills(enemy)

            if enemy.health <= 0:
                break
            print("\nEnemy HP:{0.health}.".format(enemy))
            enemy.skills(pet)

            if pet.health <= 0:
                break
            print("\nPet HP:{0.health}.".format(pet))

        if pet.health > 0:
            print("\nYou defeated the enemy!")

        if enemy.health > 0:
            print("\nYou were defeated by the enemy!")

    if __name__ == '__main__':
        combatSystem(Pet(), Mobs())


