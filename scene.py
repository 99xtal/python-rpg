class Scene:
    def __init__(self):
        self.title = ''
        self.description = ''
        self.text = ''
        self.contains_combat = None
        self.boss = None
        self.splash_screen = ''
        self.actions = None

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_text(self, text_list):
        self.text = text_list

    def set_combat(self, bool):
        self.contains_combat = bool

    def set_boss(self, boss):
        self.boss = boss

    def set_splash_screen(self, ascii):
        self.splash_screen = ascii

    def set_actions(self, actions_list):
        self.actions = actions_list
        
    def print_scene(self):
        print(f'''
        |-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_
        {self.splash_screen}
                            {self.title}

        |-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_

        {self.description}
        ''')
