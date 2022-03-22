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
        self.add_to_story(self.prologue())
        self.add_to_story(self.hercules_meets_king())
        self.add_to_story(self.hercules_vs_lion())

    def add_to_story(self, scene):
        self.scenes.append(scene)

    def title_menu(self):
        title_menu = Scene()
        title_menu.set_title("A TEXT-BASED BLOODBATH")
        title_menu.set_description("Welcome to HERCULES, a text-based role playing game in which you will\n\tplay as the titular hero as you fight ancient monsters. Will you live\n\tto slay the beasts and become a demigod, or die in vain?")
        title_menu.set_splash_screen(self.artwork.game_title())
        title_menu.set_actions(['start','quit'])
        return title_menu

    def prologue(self):
        prologue_scene = Scene()
        prologue_scene.set_title("THE LONG ROAD FROM DELPHI...")
        prologue_scene.set_description("You are walking south down a dirt road. The wilderness surrounds you,\n\tand despair plagues your soul.")
        prologue_scene.set_splash_screen(self.artwork.wilderness())
        prologue_scene.set_actions(['prev', 'next'])
        return prologue_scene

    def hercules_meets_king(self):
        h_m_k_scene = Scene()
        h_m_k_scene.set_title("THE COURT OF KING EURYSTHEUS")
        h_m_k_scene.set_description("KING:\tWho are you? How dare you enter the court of the glorious\n\t\tMycenaean King?\n\n\tHERC:\tO wise king, I am Hercules. I have asked the god Apollo\n\t\tfor penance, and he has granted it to me in the form of\n\t\tservice to you for twelve years. How may I serve you?\n\n\tKING:\tUh... yeah sure that sounds great. How about you go out and\n\t\tkill the lion at Nemea for me?")
        h_m_k_scene.set_splash_screen(self.artwork.king())
        h_m_k_scene.set_actions(['prev', 'next'])
        return h_m_k_scene

    def hercules_vs_lion(self):
        h_v_l_scene = Scene()
        h_v_l_scene.set_title("HERCULES faces the NEMEAN LION")
        h_v_l_scene.set_description("You prepare for battle...")
        h_v_l_scene.set_combat(True)
        h_v_l_scene.set_splash_screen(self.artwork.lion())

        nemean_lion = Character("Nemean Lion", 50, 50, 25, {"Claw Strike":"The lion strikes you with his claw", "Power Bite": "The lion rips off one of your fingers with its poweful bite"})
        h_v_l_scene.set_boss(nemean_lion)
        return h_v_l_scene

    def victory(self, boss):
        victory = Scene()
        victory.set_title(f"HERCULES has defeated the {boss.name.upper()}!")
        victory.set_splash_screen(self.artwork.victory())
        return victory

    def defeat(self, boss):
        defeat = Scene()
        defeat.set_title(f"HERCULES has been slain by the {boss.name.upper()}!")
        defeat.set_splash_screen(self.artwork.defeat())
        return defeat