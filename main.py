import sys
import ascii_art
from character import Character
from scene import Scene


def attack(character1, character2):
	while(True):
		character2.take_damage(character1.input_attack())
		if not character2.is_alive:
			return character1
		character1.take_damage(character2.random_attack())
		if not character1.is_alive:
			return character2

def print_combat_result(winner, enemy):
	if winner.name == "Hercules":
		victory = Scene(f"{winner.name.upper()} has defeated the {enemy.name.upper()}!", '', False, None, ascii_art.victory())
		victory.print_scene()
		winner.reset_health()
		winner.attack_power += 15
	else:
		defeat = Scene(f"HERCULES was slain by the {enemy.name.upper()}", '', False, None, ascii_art.defeat())
		defeat.print_scene()

def run_game():
	# Characters
	hercules = Character("Hercules", 100, 100, 25, {"Furious Blade":"You strike at the heart of the beast with a rage that knows no bounds", "Olympian Strike":"You slash at the beast", "Thunder of Zeus": "Lightning strkes your blade as you lift your sword to the sky"})
	lion = Character("Nemean Lion", 50, 50, 25, {"Claw Strike":"The lion strikes you with his claw", "Power Bite": "The lion rips off one of your fingers with its poweful bite"}, ascii_art.ascii_lion())
	hydra = Character("Lernaean Hydra", 75, 75, 35, {"Venemous Bite": "The hydra bites you with its venemous fangs.", "Poison Gas": "The hydra emits a cloud of poisonous gas from its lungs, stinging your eyes and skin."})

	# Scenes
	hercules_vs_lion = Scene("HERCULES faces the NEMEAN LION", "You prepare for battle...", True, lion, ascii_art.ascii_lion())
	hercules_vs_hydra = Scene("HERCULES faces the LERNAEAN HYDRA", "You prepare for battle...", True, hydra)

	scenes = [hercules_vs_lion, hercules_vs_hydra]
	# Display story and fight scenes
	
	for scene in scenes:
		scene.print_scene()
		if scene.contains_combat:
			battle = attack(hercules, scene.boss)
			print_combat_result(battle, scene.boss)
	
	# hercules_vs_lion.print_scene()
	# lion_battle = attack(hercules, lion)
	# print_combat_result(lion_battle, lion)

	# hydra_battle = attack(hercules, hydra)
	# print_combat_result(hydra_battle, hydra)

def start():
	title_card = Scene("A Text-Based Bloodbath", "Welcome to HERCULES, a text-based role playing game in which you \n\tplay as the titular hero.", False, None, ascii_art.game_title())
	title_card.print_scene()
	start_or_quit = input("\tType 'start' to start the game, type 'quit' to exit\n\t>>> ")
	if start_or_quit.lower() == "start":
		run_game()
	if start_or_quit.lower() == "quit":
		sys.exit()

start()