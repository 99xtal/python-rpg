from operator import contains


class Scene:
    def __init__(self, title, description, contains_combat=False, boss=None, splash_screen = ''):
        self.title = title
        self.description = description
        self.contains_combat = contains_combat
        self.boss = boss
        self.splash_screen = splash_screen

    def print_scene(self):
        print(f'''
        |-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_
        
        {self.splash_screen}
                            {self.title}

        |-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_

        {self.description}
        --------------------------------------------------------------------''')