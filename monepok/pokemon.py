'''
Has all the class definitions and sets up instances.
'''
from random import randint



class Pokemon():
    """The parent (superclass) Pokemon type."""

    def __init__(self, health, attack_power, name):
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.name = name
        self.type = ''
        self.attacks = []
        self.init_attacks()

    def __str__(self):
        return (f"{self.name}({self.type}) with health {self.health} "
                f"and attack {self.attack_power}.")

    # just the name no stats. Used in print function calls.
    def attacker_name(self):
        '''returns the name of the pokemon'''
        return self.name

    def attack_types(self):
        '''returns the attacks this pokemon has'''
        return self.attacks

    def dead(self):
        '''returns that the pokemon has died'''
        return self.health == 0

    # Pokemon will only heal or attack. Players must switch them.
    def heal(self, player, healing):
        '''adds to the pokemons current health'''
        self.health = min(self.health + healing, self.max_health)
        print(f"{player} heals {self.attacker_name()}.")

    def attack(self, attack, other_player):
        '''attacks another pokemon by calling other functions'''
        print(
            f"{self.attacker_name()} attacking {other_player.attacker_name()}"
            f" with {attack.name}.")
        damage = attack.calculate_damage(self.attack_power)
        self.do_damage_to(other_player, damage)

    # Rock, paper, scissors style of extra damage. Each Pokemon type is
    # stronger against one other type.
    def normal_damage(self, damage):
        '''takes damage out of health and prints the damage done'''
        self.health = max(self.health - damage, 0)
        print(f"{damage} damage done to {self.attacker_name()}")

    def extra_damage(self, amount):
        '''takes damage out of health after increasing the damage and prints the damage done'''
        damage = round(amount * 1.5)
        self.health = max(self.health - damage, 0)
        print(
            f"{damage} including extra damage done to {self.attacker_name()}")


    def lower_damage(self, amount):
        '''takes damage out of health after decreasing the damage and prints the damage done'''
        damage = round(amount *.5)
        self.health = max(self.health - damage, 0)
        print(
            f"{damage} including lowered damage done to {self.attacker_name()}")
    # default is normal damage for all types of attackers
    def grass_damage(self, amount):
        '''defaults grass damage as normal damage'''
        self.normal_damage(amount)

    def water_damage(self, amount):
        '''defaults water damage as normal damage'''
        self.normal_damage(amount)

    def fire_damage(self, amount):
        '''defaults fire damage as normal damage'''
        self.normal_damage(amount)

    def steel_damage(self, amount):
        '''defaults steel damage as normal damage'''
        self.normal_damage(amount)

    def ground_damage(self, amount):
        '''defaults ground damage as normal damage'''
        self.normal_damage(amount)

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
        '''Calculates how much damage '''
        if randint(1, 100) <= self.accuracy:
            max_damage = round(attack_power * self.power_percent / 100)
            return randint(1, max_damage)
        return 0  # Ha Ha missed me

class GrassType(Pokemon):
    """
    Grass type Pokemon are instances of this class. They have
    Leaf Storm, Mega Drain, and Razor Leaf attacks.
    """
    type = 'grass'

    # add the 3 attack types to each pokemon of this type. Notice that
    # this initialization is called by __init__ in the superclass Pokemon.
    def init_attacks(self):
        '''initiliazies attacks for grass pokemon'''
        grass_attacks = [
        Attack("Frenzy Plant", 150, 20),
        Attack("Leaf Blade", 90, 50),
        Attack("Razor Leaf", 55, 70),
        Attack("Vine Whip", 45, 85),
        Attack("Mega Drain", 40, 90),
        Attack("Bullet Seed", 25, 100),
        ]
        atck1 = randint(0, 5)
        atck2 = atck1
        while atck2 == atck1:
            atck2 = randint(0, 5)
        atck3 = atck1
        while atck3 in (atck1, atck2):
            atck3 = randint(0, 5)
        self.attacks = [grass_attacks[atck1], grass_attacks[atck2], grass_attacks[atck3]]

    # Grass Pokemon always do grass damage
    def do_damage_to(self, other_player, amount):
        '''Calls the grass damage function on the other player to do damage'''
        other_player.grass_damage(amount)

    # Override default to do extra damage if fire attacks me
    def fire_damage(self, amount):
        self.extra_damage(amount)

    def grass_damage(self, amount):
        self.lower_damage(amount)

class WaterType(Pokemon):
    """
    Water type Pokemon are instances of this class. They have
    Surf, Bubble and Hydro Pump attacks.
    """
    type = 'water'
    # add the 3 attack types to each pokemon of this type. Notice that
    # this initialization is called by __init__ in the superclass Pokemon.
    def init_attacks(self):
        '''initiliazies attacks for water pokemon'''
        water_attacks = [
        Attack("Waterfall", 120, 25),
        Attack("Water Shuriken", 100, 40),
        Attack("Surf", 90, 50),
        Attack("Muddy Water", 75, 60),
        Attack("Aqua Jet", 55, 70),
        Attack("Water Gun", 40, 100),
        ]
        atck1 = randint(0, 6)
        atck2 = atck1
        while atck2 == atck1:
            atck2 = randint(0, 5)
        atck3 = atck1
        while atck3 in (atck1, atck2):
            atck3 = randint(0, 5)
        self.attacks = [water_attacks[atck1], water_attacks[atck2], water_attacks[atck3]]

    # Water Pokemon always do water damage
    def do_damage_to(self, other_player, amount):
        '''calls the water damage function on the other player to do damage'''
        other_player.water_damage(amount)

    # Override default to do extra damage if fire attacks me
    def grass_damage(self, amount):
        self.extra_damage(amount)

    def water_damage(self, amount):
        self.lower_damage(amount)

class FireType(Pokemon):
    """
    Fire type Pokemon are instances of this class. They have
    Ember, Fire Punch, and Flame Wheel attacks.
    """
    type = 'fire'
    # add the 3 attack types to each pokemon of this type. Notice that
    # this initialization is called by __init__ in the superclass Pokemon.
    def init_attacks(self):
        '''initiliazies attacks for fire pokemon'''
        fire_attacks = [
        Attack("Sacred Fire", 110, 25),
        Attack("Sizzly Slide", 100, 40),
        Attack("Heat Wave", 90, 50),
        Attack("Blaze Kick", 85, 55),
        Attack("Fire Punch", 75, 60),
        Attack("Fire Fang", 65, 100),
        ]
        atck1 = randint(0, 5)
        atck2 = atck1
        while atck2 == atck1:
            atck2 = randint(0, 5)
        atck3 = atck1
        while atck3 in (atck1, atck2):
            atck3 = randint(0, 5)
        self.attacks = [fire_attacks[atck1], fire_attacks[atck2], fire_attacks[atck3]]
    # Grass Pokemon always do grass damage
    def do_damage_to(self, other_player, amount):
        '''calls the fire damage function on the other player to do damage'''
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
        '''initiliazies attacks for ground pokemon'''
        ground_attacks = [
        Attack("Earthquake", 110, 25),
        Attack("Dig", 90, 35),
        Attack("Stomping Tantrum", 75, 45),
        Attack("Scorching Sands", 70, 55),
        Attack("Drill Run", 60, 75),
        Attack("Bone Club", 50, 100),
        ]
        atck1 = randint(0, 5)
        atck2 = atck1
        while atck2 == atck1:
            atck2 = randint(0, 5)
        atck3 = atck1
        while atck3 in (atck1, atck2):
            atck3 = randint(0, 5)
        self.attacks = [ground_attacks[atck1], ground_attacks[atck2], ground_attacks[atck3]]

    # Grass Pokemon always do grass damage
    def do_damage_to(self, other_player, amount):
        '''calls the ground damage on the other player to do damage'''
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
        '''initiliazies attacks for steel pokemon'''
        steel_attacks = [
        Attack("Steel Beam", 140, 20),
        Attack("Steel Roller", 110, 25),
        Attack("Iron Tail", 90, 35),
        Attack("Anchor shot", 80, 40),
        Attack("Steel Wing", 70, 55),
        Attack("Metal Claw", 50, 100),
        ]
        atck1 = randint(0, 5)
        atck2 = atck1
        while atck2 == atck1:
            atck2 = randint(0, 5)
        atck3 = atck1
        while atck3 in (atck1, atck2):
            atck3 = randint(0, 5)
        self.attacks = [steel_attacks[atck1], steel_attacks[atck2], steel_attacks[atck3]]

    # Grass Pokemon always do grass damage
    def do_damage_to(self, other_player, amount):
        '''calls the steel damage function on the other player to do damage'''
        other_player.steel_damage(amount)

    # Override default to do extra damage if fire attacks me
    def fire_damage(self, amount):
        self.extra_damage(amount)

    def steel_damage(self, amount):
        self.lower_damage(amount)



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
