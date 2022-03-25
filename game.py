import sys
import time

from story import Story
from character import Character

class Game:
    def __init__(self):
        self.story = Story()
        self.current_scene_marker = 0
        self.player = Character("Hercules", 100, 100, 50, {"furious blade":"You strike at the heart of the beast with a rage that knows no bounds", "olympian strike":"You slash at the beast", "thunder of zeus": "Lightning strkes your blade as you lift your sword to the sky"})

    def run_game(self):
        '''Main game loop'''
        while(True):
            current_scene = self.story.scenes[self.current_scene_marker]
            current_scene.print_scene()
            if current_scene.contains_combat:
                self.run_combat(current_scene)
            else:
                current_scene.print_actions()
                self.prompt_action(current_scene)

    def run_combat(self, scene):
        winner = self.boss_fight(scene.boss)
        self.print_combat_result(winner, scene.boss)

        self.player.reset_health()
        scene.boss.reset_health()
        if winner.name == self.player.name:
            self.current_scene_marker += 1
        else:
            self.current_scene_marker = 0

    def boss_fight(self, boss):
        '''Character fights boss, until either health reaches zero'''
        while(True):
            boss.take_damage(self.player.input_attack())
            if not boss.is_alive:
                return self.player
            self.player.take_damage(boss.random_attack())
            if not self.player.is_alive:
                return boss

    def print_combat_result(self, winner, boss):
        '''Print 'victory' or 'defeat' screen to console'''
        if winner.name == "Hercules":
            self.story.victory(boss).print_scene()
            time.sleep(3)
        else:
            self.story.defeat(boss).print_scene()
            time.sleep(3)

    def prompt_action(self, scene):
        while(True):
            user_input = input("\t>>> ").lower()
            if user_input in scene.actions:
                if user_input == "start":
                    self.current_scene_marker = 1
                    break
                elif user_input == "next":
                    self.current_scene_marker += 1
                    break
                elif user_input == "prev":
                    self.current_scene_marker -= 1
                    break
                elif user_input == "quit":
                    sys.exit()
                elif user_input == "restart":
                    self.current_scene_marker = 0
                    break
            else:
                print("\tPlease select from the options above")