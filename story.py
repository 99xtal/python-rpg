from scene import Scene
from character import Character
from artwork import Artwork

class Story:
    def __init__(self):
        self.scenes = []
        self.artwork = Artwork()
        self.create_story()

    def create_story(self):
        '''Assemble list of strings'''
        self.scenes = [self.title_menu(),
                        self.prologue(),
                        self.hercules_meets_king(),
                        self.hercules_vs_lion(),
                        self.hercules_returns_with_lion(),
                        self.hercules_vs_hydra(),
                        self.hercules_returns_with_hydra(),
                        self.hercules_vs_cerberus(),
                        self.hercules_returns_with_cerberus(),
                        self.hercules_leaves_mycenae(),
                        self.the_end()]

    def title_menu(self):
        '''Create title menu scene'''
        return Scene().set_title("A TEXT-BASED BLOODBATH") \
                        .set_description("Welcome to HERCULES, a text-based role playing game in which you will\n\tplay as the titular hero as you fight ancient monsters. Will you live\n\tto slay the beasts and become a demigod, or die in vain?") \
                        .set_splash_screen(self.artwork.game_title()) \
                        .set_actions(['start','quit']) 

    def prologue(self):
        '''Create prologue scene'''
        return Scene().set_title("THE LONG ROAD FROM DELPHI...") \
                        .set_description("You are walking south down a dirt road. The unforgiving wilderness\n\tsurrounds you, plunging your soul in deep despair.\n\n\tAlso the fact that Hera placed a curse of madness on you that led you\n\tto kill your wife and child has you feeling pretty bummed, too...\n\n\tSoon you will reach the city of Mycenae, where you will meet the king.") \
                        .set_splash_screen(self.artwork.wilderness()) \
                        .set_actions(['prev', 'next'])

    def hercules_meets_king(self):
        '''Create first hercules/king scene'''
        return Scene().set_title("THE COURT OF KING EURYSTHEUS") \
                        .set_description("KING:\tWho are you? How dare you enter the court of the glorious\n\t\tMycenaean King?\n\n\tHERC:\tO wise king, I am Hercules. I have asked the god Apollo\n\t\tfor penance, and he has granted it to me in the form of\n\t\tservice to you for twelve years. How may I serve you?\n\n\tKING:\tUh... yeah sure that sounds great. How about you go out and\n\t\tkill the lion at Nemea for me?") \
                        .set_splash_screen(self.artwork.king()) \
                        .set_actions(['prev', 'next'])

    def hercules_vs_lion(self):
        '''Create lion combat scene'''
        nemean_lion = Character("Nemean Lion", 50, 50, 25, {"Claw Strike":"The lion strikes you with his claw", "Power Bite": "The lion rips off one of your fingers with its poweful bite"})

        return Scene().set_title("HERCULES faces the LION") \
                        .set_description("You prepare for battle...") \
                        .set_combat(True) \
                        .set_splash_screen(self.artwork.lion()) \
                        .set_boss(nemean_lion)

    def hercules_returns_with_lion(self):
        '''Create second hercules/king scene'''
        return Scene().set_title("HERCULES RETURNS") \
                        .set_description("HERC:\tMy king, I have returned with the head of the Lion of Nemea,\n\t\tas you so dutifully requested.\n\n\tKING:\tWhat?\n\n\tKING:\tOh yeah, the lion. You know you really didn't need to bring\n\t\tthe head back. It's dripping everywhere...\n\n\tKING:\tBut why don't you go out to Lerna to kill the hydra?\n\n\tHERC:\tAs you wish, your highness...\n\n\tKING:\t*shouting* Hey can we get somebody to clean this up?") \
                        .set_splash_screen(self.artwork.king()) \
                        .set_actions(['next'])

    def hercules_vs_hydra(self):
        '''Create hydra combat scene'''
        hydra = Character("Lernaen Hydra", 70, 70, 35, {"Poison Spit": "The hydra spits a poisonous spray, stinging your eyes", "Tail Whip": "The hydra hits you with it's forceful tail, knocking you down."})

        return Scene().set_title("HERCULES faces the HYDRA") \
                        .set_description("You prepare for battle...") \
                        .set_combat(True) \
                        .set_boss(hydra) \
                        .set_splash_screen(self.artwork.hydra())
    
    def hercules_returns_with_hydra(self):
        '''Create third hercules/king scene'''
        return Scene().set_title("HERCULES RETURNS AGAIN...") \
                        .set_description("HERC:\tMy king, I have returned with a head of the Hydra of Lerna.\n\n\tKING:\tReally?? Again with the heads. Didn't we talk about this?\n\n\tHERC:\tYour highness, you never said I--\n\n\tKING:\tYou know what? It doesn't matter. Just go out to the\n\t\tunderworld and kill the guard dog, Cerberus.\n\n\tKING:\t*whispering* That should keep him occupied for a bit...\n\n\tHERC:\tWhat was that?\n\n\tKING:\tNever mind that, just get out of here! And NO HEADS this time!") \
                        .set_splash_screen(self.artwork.king_angry()) \
                        .set_actions(['next'])

    def hercules_vs_cerberus(self):
        '''Create cerebus combat scene'''
        cerberus = Character("Cerberus", 100, 100, 50, {"Tail Bite": "The snake from Cerberus' tail attacks you with it's venemous bite", "Paw Stomp": "Cerberus steps on you with it's monstrous paw, crushing your ribcage"})

        return Scene().set_title("HERCULES faces CERBERUS") \
                        .set_description("You prepare for battle...") \
                        .set_combat(True) \
                        .set_boss(cerberus) \
                        .set_splash_screen(self.artwork.cerberus())

    def hercules_returns_with_cerberus(self):
        '''Create fourth hercules/king scene'''
        return Scene().set_title("HERCULES RETURNS YET AGAIN...") \
                        .set_description("HERC:\tMy king, I have returned from the underworld with the head of--\n\n\tKING:\tSeriously?? Come ON. I told you SPECIFICALLY not to bring me\n\t\tCerberus' head. And what do you do? Drop an enormous bloody\n\t\thead right on my nice parquet floors.\n\n\tHERC:\tWhat foul beast shall I slay next?\n\n\tKING:\tYou know what? I'm done. This is way more trouble than\n\t\tit's worth.\n\n\tHERC:\tBut sire, what about my 12 year contract?\n\n\tKING:\tContract? Get out of here! I'll just get someone who isn't\n\t\tbrain-dead do the rest for me...\n\n\tHERC:\tWhat about the penance for my homicidal ways?\n\n\tKING:\tWhataver, your sins are absolved. Just PLEASE leave and\n\t\tNEVER come back...") \
                        .set_splash_screen(self.artwork.king_angrier()) \
                        .set_actions(['next'])

    def hercules_leaves_mycenae(self):
        '''Create final scene'''
        return Scene().set_title("HERCULES IS THE BEST") \
                        .set_description("You leave the city of Mycenae feeling good about yourself.\n\n\tAfter all, you did kill all those beasts, bringing the back the heads\n\tjust like the King asked you too.\n\n\tYou think about what a good impression you left on the King. You\n\tthink he really likes you. Maybe you'll come back another time to say\n\thi.\n\n\tAs for now, you'll walk back home to see your wife and--\n\n\tOh wait, yeah, you killed them...\n\n\tUh, you guess you'll just walk back to Mycenae to see if the King\n\tneeds anything...") \
                        .set_splash_screen(self.artwork.wilderness()) \
                        .set_actions(['prev','next'])

    def the_end(self):
        '''Create end screen'''
        return Scene().set_splash_screen(self.artwork.end()) \
                        .set_actions(['restart', 'quit'])

    def victory(self, boss):
        '''Create victory screen'''
        return Scene().set_title(f"HERCULES has defeated the {boss.name.upper()}!") \
                        .set_splash_screen(self.artwork.victory())

    def defeat(self, boss):
        '''Create defeat screen'''
        return Scene().set_title(f"HERCULES has been slain by the {boss.name.upper()}!") \
                        .set_splash_screen(self.artwork.defeat())
