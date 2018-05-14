import actors
import random

def main():

    print_header()
    game_loop()


def print_header():
    print('-'*15)
    print('     WIZARD GAME')
    print('-'*15)
    print()

def game_loop():
    creatures = [
        actors.Creature('Bat', 5),
        actors.Creature('Toad', 5),
        actors.Creature('Tiger', 12),
        actors.Dragon('Black Dragon', 50, scaliness =2, breaths_fire = False),
        actors.Wizard('Evil Wizard', 1000),

    ]

    hero = actors.Wizard("Gandolf", 75)

    while True:

        active_creature = random.choice(creatures)
        print(active_creature)


if __name__ == '__main__':
    main()
