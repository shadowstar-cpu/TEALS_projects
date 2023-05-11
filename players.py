"""
A Player will be of type user or computer. 
You could have a user play against the computer or 
have two players depending on which you instatiate.
You could also have two computer players fight.
"""

from random import choice
from pokemon import pocket_monsters


class Player():

    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.choose_3_pokemon()
        self.choose_attacker()

    def __str__(self):
        return self.name

    def take_a_turn_against(self, other_player):
        print()  # skip a line to make it legible
        self.your_move(other_player)
        if not other_player.game_over():
            other_player.take_a_turn_against(self)
        else:
            show_pokemon(self, other_player)
            print(f"{self} wins the game.")

    def make_a_move(self, move, other_player):
        if move == 'a':
            print(f"{self} chooses to attack.")
            self.attack(other_player)

        elif move == 'h':
            print(f"{self} chooses to heal {self.attacker_name()}.")
            self.heal()

        elif move == 's':
            print(f"{self} chooses to switch Pokemon.")
            self.switch()

        elif move == 'p':
            # showing current Pokemon status. This doesn't cost a turn.
            show_pokemon(self, other_player)
            self.your_move(other_player)

        else:
            # recursively ask for a different move.
            print("I don't know that one.")
            self.your_move(other_player)

    def game_over(self):
        return (self.pokemon[0].dead() and self.pokemon[1].dead()
                and self.pokemon[2].dead())

    # Three different commands a player can choose.
    # attack and heal are redirected to the Pokemon.
    # If attacking Pokemon has been knocked out force a switch.
    # A forced switch stills costs a turn.
    def switch(self):
        self.choose_attacker()
        print(f"{self} chooses {self.attacker_name()}")

    def attack(self, other_player):
        if self.attacker.dead():
            print(
                f"Sorry {self}, your Pokemon was knocked out. You must switch."
            )
            self.switch()
        else:
            self.attacker.attack(self.choose_attack(), other_player)

    def heal(self):
        if self.attacker.dead():
            print(
                f"Sorry {self}, your Pokemon was knocked out. You must switch."
            )
            self.switch()
        else:
            self.attacker.heal(self, 20)

    # redirect damage taken to the active Pokemon
    def fire_damage(self, damage):
        self.attacker.fire_damage(damage)

    def grass_damage(self, damage):
        self.attacker.grass_damage(damage)

    def water_damage(self, damage):
        self.attacker.water_damage(damage)
    
    def steel_damage(self, damage):
        self.attacker.steel_damage(damage)

    def ground_damage(self, damage):
        self.attacker.ground_damage(damage)

    # active Pokemon name, just the name.
    def attacker_name(self):
        return self.attacker.attacker_name()


"""
User type players will always ask for choices and commands.
"""


class User(Player):

    def your_move(self, other_player):
        print(f"Player {self.name} your move.")
        move = input("Attack (a), heal (h), switch (s) or Pokemon status (p)?")
        self.make_a_move(move, other_player)

    def choose_3_pokemon(self):
        for i in range(3):
            monster = choose_pokemon(pocket_monsters)
            self.pokemon.append(monster)
            pocket_monsters.remove(monster)

    def choose_attacker(self):
        print("Who will attack?")
        self.attacker = choose_pokemon(self.pokemon)

    def choose_attack(self):
        print("Choose your attack!")
        return choose_attack(self.attacker.attack_types())


"""
Computer players will just randomly take actions.
They might not be intelligent actions, just actions.
"""


class Computer(Player):

    def your_move(self, other_player):
        print(f"Player {self.name} next move.")
        self.make_a_move(choice(['a', 'a', 'a', 'a', 'h', 's']), other_player)

    def choose_3_pokemon(self):
        for i in range(3):
            monster = choice(pocket_monsters)
            self.pokemon.append(monster)
            pocket_monsters.remove(monster)

    def choose_attacker(self):
        self.attacker = choice(self.pokemon)
        if self.attacker.health <= 0:
            self.choose_attacker()

    def choose_attack(self):
        return choice(self.attacker.attack_types())


"""
User interface functions. 
Choose a pokemon. Choose an attack.
"""


def choose_pokemon(pokemon):
    """Choose one of several Pokemon."""
    print("Enter the number for your pokemon choice.")
    for i, monster in enumerate(pokemon):
        print(f"{i+1}. {monster}")
    index = int(input("Choose? "))
    if index < 1 or index > len(pokemon):
        print("Not a valid number.")
        return choose_pokemon(pokemon)
    elif pokemon[index - 1].dead():
        print("That Pokemon is already knocked out, choose another.")
        return choose_pokemon(pokemon)
    else:
        return pokemon[index - 1]


def choose_attack(attacks):
    """Choose one of three attacks."""
    print("Enter the number for your attack choice.")
    for i, attack in enumerate(attacks):
        print(f"{i+1}. {attack}")
    index = int(input("Choose? "))
    if index < 1 or index > len(attacks):
        print("Not a valid number.")
        return choose_attack(attacks)
    else:
        return attacks[index - 1]


# a fourth command is to show the current status
def show_pokemon(player_1, player_2):
    show_title()
    print(f"{player_1} attacking with {player_1.attacker_name()}")
    print("Pokemon are:")
    for monster in player_1.pokemon:
        print("   " + str(monster))
    print()
    print(f"{player_2} attacking with {player_2.attacker_name()}")
    print("Pokemon are:")
    for monster in player_2.pokemon:
        print("   " + str(monster))
    print()


def show_title():
    print("""
                                  ,'\\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
          """)