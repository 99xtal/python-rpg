from turtle import title
from scene import Scene
from character import Character
from artwork import Artwork

class Story:
    def __init__(self):
        self.scenes = []
        self.artwork = Artwork()
        self.create_story()

    def create_story(self):
        self.add_to_story(self.title_menu())
        self.add_to_story(self.hercules_vs_lion())

    def add_to_story(self, scene):
        self.scenes.append(scene)

    def title_menu(self):
        title_menu = Scene()
        title_menu.add_title("A Text-Based Bloodbath")
        title_menu.add_description("Welcome to HERCULEs, a text-based role playing game in which you will\n\tplay as the titular hero as you fight ancient monsters. Will you live\n\tto become a demigod, or die in vain?")
        title_menu.set_splash_screen(self.artwork.game_title())
        return title_menu

    def hercules_vs_lion(self):
        h_v_l_scene = Scene()
        h_v_l_scene.add_title("HERCULES faces the NEMEAN LION")
        h_v_l_scene.add_description("You prepare for battle...")
        h_v_l_scene.set_combat(True)
        h_v_l_scene.set_splash_screen(self.artwork.lion())

        nemean_lion = Character("Nemean Lion", 50, 50, 25, {"Claw Strike":"The lion strikes you with his claw", "Power Bite": "The lion rips off one of your fingers with its poweful bite"})
        h_v_l_scene.set_boss(nemean_lion)
        return h_v_l_scene

    def victory(self, boss):
        victory = Scene()
        victory.add_title(f"HERCULES has defeated the {boss.name.upper()}!")
        victory.set_splash_screen(self.artwork.victory())
        return victory

    def defeat(self, boss):
        defeat = Scene()
        defeat.add_title(f"HERCULES has been slain by the {boss.name.upper()}!")
        defeat.set_splash_screen(self.artwork.defeat())
        return defeat