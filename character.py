import random
import time

def list_attack_names(attack_names):
    attack_str = ''
    for i in attack_names:
        attack_str += f"\t[{i}]\n"
    return attack_str

def generate_attack_damage(attack_power):
    d20_roll = random.random()
    return int(attack_power * d20_roll)

class Character:
    def __init__(self, name, health, max_health, attack_power, attack_names, icon=''):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.attack_power = attack_power
        self.attack_names = attack_names
        self.icon = icon
        self.is_alive = True

    def input_attack(self):
        attack_choice = input(f"\tHow will you attack your foe?\n\n{list_attack_names(self.attack_names)}\n\n\t>>> ")
        print(f"\t{self.name.upper()} uses {attack_choice.upper()}!")
        print(f"\t{self.attack_names[attack_choice]}")
        time.sleep(1)
        return generate_attack_damage(self.attack_power)

    def random_attack(self):
        random_attack_choice = random.randrange(0,len(self.attack_names))
        attack_name_key_list = list(self.attack_names)
        random_attack_name = attack_name_key_list[random_attack_choice]
        print(f"\t{self.name.upper()} uses {random_attack_name.upper()}!")
        print(f"\t{self.attack_names[random_attack_name]}")
        time.sleep(1)
        return generate_attack_damage(self.attack_power)

    def take_damage(self, damage):
        if (damage > self.health):
            self.health = 0
            self.is_alive = False
        else:
            self.health -= damage
        print(f"\n\t{self.name.upper()} takes {damage}hp of damage!\tHealth Remaining: ({self.health}/{self.max_health})\n")
        time.sleep(1)

    def reset_health(self):
        self.health = self.max_health