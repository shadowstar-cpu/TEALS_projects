"""
You will be working with this file. 
1. Add the WaterType Pokemon.
2. Add the FireType Pokemon.
3. Instantiate 9 Pokemon, 3 of each type.
"""
"""
Pokemon!!! The Pokemon class does almost everything.
Subclasses are of types grass, fire, or water.
Each type has different abilities.
"""

from random import randint


class Pokemon():
    """The parent (superclass) Pokemon type."""

    def __init__(self, health, attack_power, name):
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.name = name
        self.init_attacks()

    def __str__(self):
        return (f"{self.name}({self.type}) with health {self.health} "
                f"and attack {self.attack_power}.")

    # just the name no stats. Used in print function calls.
    def attacker_name(self):
        return self.name

    def attack_types(self):
        return self.attacks

    def dead(self):
        return self.health == 0

    # Pokemon will only heal or attack. Players must switch them.
    def heal(self, player, healing):
        self.health = min(self.health + healing, self.max_health)
        print(f"{player} heals {self.attacker_name()}.")

    def attack(self, attack, other_player):
        print(
            f"{self.attacker_name()} attacking {other_player.attacker_name()}"
            f" with {attack.name}.")
        damage = attack.calculate_damage(self.attack_power)
        self.do_damage_to(other_player, damage)

    # Rock, paper, scissors style of extra damage. Each Pokemon type is
    # stronger against one other type.
    def normal_damage(self, damage):
        self.health = max(self.health - damage, 0)
        print(f"{damage} damage done to {self.attacker_name()}")

    def extra_damage(self, amount):
        damage = round(amount * 1.5)
        self.health = max(self.health - damage, 0)
        print(
            f"{damage} including extra damage done to {self.attacker_name()}")


    def lower_damage(self, amount):
        damage = round(amount *.5)
        self.health = max(self.health - damage, 0)
        print(
            f"{damage} including lowered damage done to {self.attacker_name()}")
    # default is normal damage for all types of attackers
    def grass_damage(self, amount):
        self.normal_damage(amount)

    def fire_damage(self, amount):
        self.normal_damage(amount)

    def water_damage(self, amount):
        self.normal_damage(amount)

    def steel_damage(self, amount):
        self.normal_damage(amount)

    def ground_damage(self, amount):
        self.normal_damage(amount)
"""
Now we define Pokemon classes of specific types. You will instantiate
these classes to create individual Pokemon. Each of these classes should
use the Pokemon class as a superclass.
Each type of Pokemon will need to store its type. Each type will Need to
implement init_attacks to create 3 attack types. Each type will need to
implement do_damage_to to tell the other Pokemon what type of damage is 
done. Each type will also need to override a specific type of damage and 
do extra to itself.
"""

""" Grass type Pokemon have leaf attacks and are weak to fire damage."""


class GrassType(Pokemon):
    """
    Grass type Pokemon are instances of this class. They have
    Leaf Storm, Mega Drain, and Razor Leaf attacks.
    """
    type = 'grass'

    # add the 3 attack types to each pokemon of this type. Notice that
    # this initialization is called by __init__ in the superclass Pokemon.
    def init_attacks(self):
        self.attacks = [
            Attack("Vine Whip", 45, 85),
            Attack("Mega Drain", 40, 90),
            Attack("Frenzy Plant", 150, 50), 
            Attack("Bullet Seed", 25, 100),
            Attack("Leaf Blade", 90, 65),
            Attack("Razor Leaf", 55, 80),
        ]

    # Grass Pokemon always do grass damage
    def do_damage_to(self, other_player, amount):
        other_player.grass_damage(amount)

    # Override default to do extra damage if fire attacks me
    def fire_damage(self, amount):
        self.extra_damage(amount)
    
    def grass_damage(self, amount):
        self.lower_damage(amount)


"""Water type Pokemon have water attacks and are weak to grass damage."""


class WaterType(Pokemon):
    """
    Water type Pokemon are instances of this class. They have
    Surf, Bubble and Hydro Pump attacks.
    """
    type = 'water'

    # add the 3 attack types to each pokemon of this type. Notice that
    # this initialization is called by __init__ in the superclass Pokemon.
    def init_attacks(self):
        self.attacks = [
            Attack("Muddy Water", 75, 85),
            Attack("Water Gun", 40, 100),
            Attack("Water Shuriken", 100, 70),
            Attack("Surf", 90, 75),
            Attack("Aqua Jet", 55, 90),
            Attack("Waterfall", 120, 55),
        ]

    # Water Pokemon always do water damage
    def do_damage_to(self, other_player, amount):
        other_player.water_damage(amount)

    # Override default to do extra damage if fire attacks me
    def grass_damage(self, amount):
        self.extra_damage(amount)

    def water_damage(self, amount):
        self.lower_damage(amount)
"""Fire type Pokemon have fire attacks and are weak to water damage."""


class FireType(Pokemon):
    """
    Fire type Pokemon are instances of this class. They have
    Ember, Fire Punch, and Flame Wheel attacks.
    """
    type = 'fire'

    # add the 3 attack types to each pokemon of this type. Notice that
    # this initialization is called by __init__ in the superclass Pokemon.
    def init_attacks(self):
        self.attacks = [
            Attack("Fire Punch", 75, 95),
            Attack("Sacred Fire", 100, 75),
            Attack("Fire Fang", 65, 100),
            Attack("Heat Wave", 90, 95),
            Attack("Sizzly Slide", 90, 100),
            Attack("Blaze Kick", 85, 90),
        ]

    # Grass Pokemon always do grass damage
    def do_damage_to(self, other_player, amount):
        other_player.fire_damage(amount)

    # Override default to do extra damage if fire attacks me
    def water_damage(self, amount):
        self.extra_damage(amount)
    
    def fire_damage(self, amount):
        self.lower_damage(amount)

class GroundType(Pokemon):
    """
    Fire type Pokemon are instances of this class. They have
    Ember, Fire Punch, and Flame Wheel attacks.
    """
    type = 'ground'

    # add the 3 attack types to each pokemon of this type. Notice that
    # this initialization is called by __init__ in the superclass Pokemon.
    def init_attacks(self):
        self.attacks = [
            Attack("Dig", 80, 90),
            Attack("Earthquake", 100, 80),
            Attack("Drill Run", 70, 95),
            Attack("Bone Club", 65, 85),
            Attack("Scorching Sands", 70, 100),
            Attack("Stomping Tantrum", 75, 100),
        ]

    # Grass Pokemon always do grass damage
    def do_damage_to(self, other_player, amount):
        other_player.ground_damage(amount)

    # Override default to do extra damage if grass attacks me
    def grass_damage(self, amount):
        self.extra_damage(amount)
    
    def ground_damage(self, amount):
        self.lower_damage(amount)

class SteelType(Pokemon):
    """
    Fire type Pokemon are instances of this class. They have
    Ember, Fire Punch, and Flame Wheel attacks.
    """
    type = 'steel'

    # add the 3 attack types to each pokemon of this type. Notice that
    # this initialization is called by __init__ in the superclass Pokemon.
    def init_attacks(self):
        self.attacks = [
            Attack("Steel Beam", 140, 65),
            Attack("Steel Wing", 70, 95),
            Attack("Steel Roller", 130, 75),
            Attack("Anchor shot", 80, 100),
            Attack("Iron Tail", 100, 75),
            Attack("Metal Claw", 50, 95),
        ]

    # Grass Pokemon always do grass damage
    def do_damage_to(self, other_player, amount):
        other_player.steel_damage(amount)

    # Override default to do extra damage if fire attacks me
    def fire_damage(self, amount):
        self.extra_damage(amount)
    
    def steel_damage(self, amount):
        self.lower_damage(amount)

"""
We are going to make objects to represent attacks. 
Damage calculations and hit/miss are done here.
Use the init_attacks method to instatiate 3 different
attacks for each new type of Pokemon.
"""


class Attack():
    """Attacks do the damage calculation."""

    def __init__(self, name, power, accuracy):
        self.name = name
        self.power_percent = power
        self.accuracy = accuracy

    def __str__(self):
        return (f"{self.name} with {self.power_percent}% of "
                f"attack power and {self.accuracy}% chance to hit.")

    def calculate_damage(self, attack_power):
        if randint(1, 100) <= self.accuracy:
            max_damage = round(attack_power * self.power_percent / 100)
            return randint(1, max_damage)
        else:
            return 0  # Ha Ha missed me


"""
Now we create a list of individual Pokemon. You will need to add 8 more.
"""
pocket_monsters = [
    WaterType(55, 45, 'Whooper'),
    WaterType(20, 10, 'Magikarp'),
    WaterType(130, 80, 'Lapras'),
    GrassType(45, 45, 'Snivy'),
    GrassType(40, 35, 'Weedle'),
    GrassType(65, 110, 'Leafion'),
    FireType(40, 50, 'Charmander'),
    FireType(115, 115, 'Entei'),
    FireType(90, 110, 'Arcanine'),
    GroundType(105, 130, 'Rhydon'),
    GroundType(35, 100, 'Dugtrio'),
    GroundType(35, 45, 'Onix'),
    SteelType(75, 85, 'Steelix'),
    SteelType(80, 75, 'Registeel'),
    SteelType(100, 110, 'Celesteela'),
]
