from character import Character

def attack(character1, character2):
	print(f'''
	####################################################################
	{character1.name.upper()} FACES THE {character2.name.upper()}...
	####################################################################''')
	
	while(True):
		character2.take_damage(character1.input_attack())
		if not character2.is_alive:
			return character1
		character1.take_damage(character2.random_attack())
		if not character1.is_alive:
			return character2


def run_game():
	# Build Hercules and enemies
	hercules = Character("Hercules", 100, 50, {"Furious Blade":"You strike at the heart of the beast with a rage that knows no bounds", "Olympian Strike":"You slash at the beast", "Thunder of Zeus": "Lightning strkes as you lift your sword to the sky"})
	lion = Character("Nemean Lion", 75, 25, {"Claw Strike":"The lion strikes you with his claw", "Power Bite": "The lion bites you"})

	# Hercules fights the lion
	hercules_vs_lion = attack(hercules, lion)


run_game()