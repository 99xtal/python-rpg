import sys
import time

from story import Story
from character import Character

class Game:
    def __init__(self):
        self.story = Story()
        self.current_scene_marker = 0
        self.player = Character("Hercules", 100, 100, 0, {"furious blade":"You strike at the heart of the beast with a rage that knows no bounds", "olympian strike":"You slash at the beast", "thunder of zeus": "Lightning strkes your blade as you lift your sword to the sky"})

    def run_game(self):
        while(True):
            current_scene = self.story.scenes[self.current_scene_marker]
            current_scene.print_scene()
            if current_scene.contains_combat:
                self.run_combat(current_scene.boss)
            self.print_scene_actions(current_scene)
            self.prompt_action(current_scene)

    def run_combat(self, boss):
        while(True):
            boss.take_damage(self.player.input_attack())
            if not boss.is_alive:
                self.print_combat_result(self.player, boss)
                break
            self.player.take_damage(boss.random_attack())
            if not self.player.is_alive:
                self.print_combat_result(boss, boss)
                sys.exit()

    def print_scene_actions(self, scene):
        actions_str = "\tACTIONS: "
        for action in scene.actions:
            actions_str += f"{action}\t"
        print(actions_str)

    def print_combat_result(self, winner, boss):
        if winner.name == "Hercules":
            self.story.victory(boss).print_scene()
        else:
            self.story.defeat(boss).print_scene()

    def prompt_action(self, current_scene):
        while(True):
            user_input = input("\t>>> ").lower()
            if user_input in current_scene.actions:
                if user_input == "start":
                    self.current_scene_marker += 1
                    break
                elif user_input == "next":
                    self.current_scene_marker += 1
                    break
                elif user_input == "prev":
                    if self.current_scene_marker > 0:
                        self.current_scene_marker -= 1
                    break
                elif user_input == "quit":
                    sys.exit()
            else:
                print("\tPlease select from the options above")