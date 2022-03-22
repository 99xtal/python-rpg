import sys
import time

from story import Story
from character import Character

class Game:
    def __init__(self):
        self.story = Story()
        self.player = Character("Hercules", 100, 100, 0, {"Furious Blade":"You strike at the heart of the beast with a rage that knows no bounds", "Olympian Strike":"You slash at the beast", "Thunder of Zeus": "Lightning strkes your blade as you lift your sword to the sky"})

    def run_game(self):
        for scene in self.story.scenes:
            scene.print_scene()
            time.sleep(3)
            if scene.contains_combat:
                self.run_combat(scene.boss)

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

    def print_combat_result(self, winner, boss):
        if winner.name == "Hercules":
            self.story.victory(boss).print_scene()
        else:
            self.story.defeat(boss).print_scene()
