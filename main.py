from character import Character

def attack(character1, character2):
	print(f'''
	|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_
				           ,  ,, ,
				  , ,; ; ;;  ; ;  ;
			   , ; ';  ;  ;; .-''\ ; ;
			, ;  ;`  ; ,; . / /8b \ ; ;
			`; ; .;'         ;,\8 |  ;  ;
			 ` ;/   / `_      ; ;;    ;  ; ;
			    |/.'  /9)    ;  ; `    ;  ; ;
			   ,/'          ; ; ;  ;   ; ; ; ;
			  /_            ;    ;  `    ;  ;
			 `?8P"  .      ;  ; ; ; ;     ;  ;;
			 | ;  .:: `     ;; ; ;   `  ;  ;
			 `' `--._      ;;  ;;  ; ;   ;   ;
			  `-..__..--''   ; ;    ;;   ; ;   ;
    					  ;    ; ; ;   ;     ;
								  
	\t\t{character1.name.upper()} FACES THE {character2.name.upper()}...
	''')
	
	while(True):
		character2.take_damage(character1.input_attack())
		if not character2.is_alive:
			return character1
		character1.take_damage(character2.random_attack())
		if not character1.is_alive:
			return character2

def combat_result(winner,hero,enemy):
	if winner.name == "Hercules":
		print(f'''
	|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_
		____   ____.__        __                       ._.
		\   \ /   /|__| _____/  |_  ___________ ___.__.| |
		 \   Y   / |  |/ ___\   __\/  _ \_  __ <   |  || |
		  \     /  |  \  \___|  | (  <_> )  | \/\___  | \|
		   \___/   |__|\___  >__|  \____/|__|   / ____| __
		                   \/                   \/      \/

			{winner.name.upper()} has defeated the {enemy.name.upper()}!
		''')
	else:
		print("defeat")

def run_game():
	# Build Hercules and enemies
	hercules = Character("Hercules", 100, 50, {"Furious Blade":"You strike at the heart of the beast with a rage that knows no bounds", "Olympian Strike":"You slash at the beast", "Thunder of Zeus": "Lightning strkes as you lift your sword to the sky"})
	lion = Character("Nemean Lion", 75, 25, {"Claw Strike":"The lion strikes you with his claw", "Power Bite": "The lion bites you"})

	# Hercules fights the lion
	hercules_vs_lion = attack(hercules, lion)
	combat_result(hercules_vs_lion, hercules, lion)


run_game()