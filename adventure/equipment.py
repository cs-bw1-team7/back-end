from enum import auto, Enum, unique
from typing import Any
import random

class Style(Enum):
    melee = 0.8
    midrange = 0.6
    longrange = 0.4


class Finish(Enum):
    light = 0.4
    medium = 0.6
    heavy = 0.8
    volcanic = rand(range(0, 0.9))

class Style_Description(Enum):
    melee="\nThis weapon is used in Melee attacks, your close combat style. \nAttacks carried out in the melee combat style will have the greatest accuracy.\n"
    midrange="\nThis weapon is used in a midrange combat style. \nAttacks carried out in the midrange combat style will have moderate accuracy.\n"
    longrange="\nThis weapon is used in a longrange combat style. \nAttacks carried out by this weapon will have low accuracy.\n"

class  Finish_Description(Enum):
    light = "This weapon has a bronze finish. Bronze weapons deliver blows that result in lower damage.\n"
    medium = "This weapon has an iron finish. Iron weapons deliver blows that result in moderate damage.\n"
    heavy = "This weapon has a steel finish. Steel weapons deliver blows that result in heavy damage.\n"
    volcanic = "This weapon has a volcanic finish. \nAttacking with a volcanic weapon is like Russian Roulette; \nYou may deliver a strong blow, or a weak one.\n May the odds be ever in your favor.\n"

class Weapon(self):
    '''
    This
    '''
    def __init__(self, name: str, style_description: str, finish_description: str, style: Style.melee, finish: finish.light)
        self.name = name
        self.style_description = random.choice(Finish)
        self.finish_description = finish_description
        self.style = style
        self.finish = finish
        
