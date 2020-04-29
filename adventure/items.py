from enum import auto
from .named_enum import NamedEnum
from .equipment import (Weapon, Style, Finish, Style_Description, Finish_Description)

class Weapons(NamedEnum):
    '''
    ===Overview===
    The weapons class handles the weapon generation and each weapon will have attributes for style and finish.
    
    ===Attributes===
    style: This attribute defines the combat style as one of 3 types
        melee: This is the close range combat style. Melee attacks will deliver blows with the greatest accuracy/chance of landing blow(0.8)
        midrange: This is your midrange combat style. Midrange attacks will deliver blows with moderate accuracy/chance of landing blow(0.6)
        projectiles: This is your long range combat style. Long range attacks will deliver blows with less accuracy/chance of landing blow(0.4)
    
    finish: This attribute defines the finish on the weapon which will define the amount of damage attacking with this weapon will deliver.
        light: This finish will deliver the least amount of damage of the 4 finishes(0.2)
        medium: This finish will deliver a moderate amount of damage(0.4).
        heavy: This finish will deliver a heavy amount of damage.
        volcanic(rand): This finish will deliver a random amount of damage (light, medium, or heavy)
    '''

    #melee Weapons (close range combat)
    #light
    bronze_wrist_blades = auto()
    bronze_knuckles = auto()
    bronze_knife = auto()
    bronze_viking_halberd = auto()
    bronze_rondel_dagger = auto()
    bronze_war_hammer = auto()
    bronze_whipping_chain = auto()

    #medium
    iron_wrist_blades = auto()
    iron_knuckles = auto()
    iron_knife = auto()
    iron_viking_halberd = auto()
    iron_rondel_dagger = auto()
    iron_war_hammer = auto()
    iron_whipping_chain = auto()

    #heavy
    steel_wrist_blades = auto()
    steel_knuckles = auto()
    steel_knife = auto()
    steel_viking_halberd = auto()
    steel_rondel_dagger = auto()
    steel_war_hammer = auto()
    steel_whipping_chain = auto()

    #volcanic
    volcanic_wrist_blades = auto()
    volcanic_knuckles = auto()
    volcanic_knife = auto()
    volcanic_viking_halberd = auto()
    volcanic_rondel_dagger = auto()
    volcanic_war_hammer = auto()
    volcanic_whipping_chain = auto()
    
    #midrange Weapons(midrange combat)
    #light
    bronze_arming_sword = auto()
    bronze_estoc = auto()
    bronze_katana = auto()
    bronze_long_sword = auto()
    bronze_rapier = auto()
    bronze_chain = auto()
    bronze_morning_star = auto()

    #medium
    iron_arming_sword = auto()
    iron_estoc = auto()
    iron_katana = auto()
    iron_long_sword = auto()
    iron_rapier = auto()
    iron_chain = auto()
    iron_morning_star = auto()

    #heavy
    steel_arming_sword = auto()
    steel_estoc = auto()
    steel_katana = auto()
    steel_long_sword = auto()
    steel_rapier = auto()
    steel_chain = auto()
    steel_morning_star = auto()

    #volcanic
    volcanic_arming_sword = auto()
    volcanic_estoc = auto()
    volcanic_katana = auto()
    volcanic_long_sword = auto()
    volcanic_rapier = auto()
    volcanic_chain = auto()
    volcanic_morning_star = auto()

    #projectile Weapons(long range combat)

    #light
    bronze_shuriken = auto()
    bronze_nzappa_zap = auto()
    bronze_longbow = auto()
    bronze_crossbow = auto()
    bronze_byzantine_flamethrower = auto()
    bronze_musket = auto()
    bronze_arquebus = auto()

    #medium
    iron_shuriken = auto()
    iron_nzappa_zap = auto()
    iron_longbow = auto()
    iron_crossbow = auto()
    iron_byzantine_flamethrower = auto()
    iron_musket = auto()
    iron_arquebus = auto()

    #heavy
    steel_shuriken = auto()
    steel_nzappa_zap = auto()
    steel_longbow = auto()
    steel_crossbow = auto()
    steel_byzantine_flamethrower = auto()
    steel_musket = auto()
    steel_arquebus = auto()

    #volcanic
    volcanic_shuriken = auto()
    volcanic_nzappa_zap = auto()
    volcanic_longbow = auto()
    volcanic_crossbow = auto()
    volcanic_byzantine_flamethrower = auto()
    volcanic_musket = auto()
    volcanic_arquebus = auto()

    weapons = {
        #melee
        #light
        Weapons.bronze_wrist_blades: Weapon(
            name=Weapons.bronze_wrist_blades.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),
        
        Weapons.bronze_knuckles: Weapon(
            name=Weapons.bronze_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Weapons.bronze_knife: Weapon(
            name=Weapons.bronze.knife.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Weapons.bronze_viking_halberd: Weapon(
            name=Weapons.bronze_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Weapons.bronze_rondel_dagger: Weapon(
            name=Weapons.bronze_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Weapons.bronze_war_hammer: Weapon(
            name=Weapons.war_hammer.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Weapons.bronze_whipping_chain: Weapon(
            name=Weapons.whipping_chain.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),
        
        #medium
        Weapons.iron_wrist_blades: Weapon(
            name=Weapons.iron_wrist_blades.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Weapons.iron_knuckles: Weapon(
            name=Weapons.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Weapons.iron_knife: Weapon(
            name=Weapons.iron_knife.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Weapons.iron_viking_halberd: Weapon(
            name=Weapons.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Weapons.iron_rondel_dagger: Weapon(
            name=Weapons.iron_rondel_dagger.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Weapons.iron_war_hammer: Weapon(
            name=Weapons.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Weapons.iron_whipping_chain: Weapon(
            name=Weapons.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        #heavy
        Weapons.steel_wrist_blades: Weapon(
            name=Weapons.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Weapons.steel_knuckles: Weapon(
            name=Weapons.steel_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Weapons.steel_knife: Weapon(
            name=Weapons.steel_knife.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Weapons.steel_viking_halberd: Weapon(
            name=Weapons.steel_viking_halberd.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Weapons.steel_rondel_dagger: Weapon(
            name=Weapons.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Weapons.steel_war_hammer: Weapon(
            name=Weapons.steel_war_hammer.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Weapons.steel_whipping_chain: Weapon(
            name=Weapons.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        #volcanic
        Weapons.volcanic_wrist_blades: Weapon(
            name=Weapons.volcanic_wrist_blades.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Weapons.volcanic_knuckles: Weapon(
            name=Weapons.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Weapons.volcanic_knife: Weapon(
            name=Weapons.volcanic_knife.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Weapons.volcanic_viking_halberd: Weapon(
            name=Weapons.volcanic_viking_halberd.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Weapons.volcanic_rondel_dagger: Weapon(
            name=Weapons.volcanic_rondel_dagger.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),
        
        Weapons.volcanic_war_hammer: Weapon(
            name=Weapons.volcanic_war_hammer.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Weapons.volcanic_whipping_chain: Weapon(
            name=Weapons.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),
        
        #midrange
        #light
        Weapons.bronze_arming_sword: Weapon(
            name=Weapons.bronze_arming_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Weapons.bronze_estoc: Weapon(
            name=Weapons.bronze_estoc.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),
        
        Weapons.bronze_katana: Weapon(
            name=Weapons.bronze_katana.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Weapons.bronze_long_sword: Weapon(
            name=Weapons.bronze_long_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Weapons.bronze_rapier: Weapon(
            name=Weapons.bronze_rapier.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Weapons.bronze_chain: Weapon(
            name=Weapons.bronze_chain.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Weapons.bronze_morning_star: Weapon(
            name=Weapons.bronze_morning_star.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),
        
        #medium
        Weapons.iron_arming_sword: Weapon(
            name=Weapons.iron_arming_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Weapons.iron_estoc: Weapon(
            name=Weapons.iron_estoc.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Weapons.iron_katana: Weapon(
            name=Weapons.bronze_katana.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.light),

        Weapons.iron_long_sword: Weapon(
            name=Weapons.iron_long_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Weapons.iron_rapier: Weapon(
            name=Weapons.iron_rapier.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Weapons.iron_chain: Weapon(
            name=Weapons.iron_chain.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Weapons.iron_morning_star: Weapon(
            name=Weapons.iron_morning_star.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),
        
        #heavy
        Weapons.steel_arming_sword: Weapon(
            name=Weapons.steel_arming_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Weapons.steel_estoc: Weapon(
            name=Weapons.steel_estoc.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Weapons.steel_katana: Weapon(
            name=Weapons.bronze_katana.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Weapons.steel_long_sword: Weapon(
            name=Weapons.steel_long_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Weapons.steel_rapier: Weapon(
            name=Weapons.steel_rapier.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Weapons.steel_chain: Weapon(
            name=Weapons.steel_chain.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Weapons.steel_morning_star: Weapon(
            name=Weapons.steel_morning_star.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),
        
        #volcanic
        Weapons.volcanic_arming_sword: Weapon(
            name=Weapons.volcanic_arming_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Weapons.volcanic_estoc: Weapon(
            name=Weapons.volcanic_estoc.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Weapons.volcanic_katana: Weapon(
            name=Weapons.bronze_katana.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Weapons.volcanic_long_sword: Weapon(
            name=Weapons.volcanic_long_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Weapons.volcanic_rapier: Weapon(
            name=Weapons.volcanic_rapier.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Weapons.volcanic_chain: Weapon(
            name=Weapons.volcanic_chain.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Weapons.volcanic_morning_star: Weapon(
            name=Weapons.volcanic_morning_star.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),
        
        #longrange
        #light
        Weapons.bronze_shuriken: Weapon(
            name=Weapons.bronze_shuriken.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Weapons.bronze_nzappa_zap: Weapon(
            name=Weapons.bronze_nzappa_zap.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Weapons.bronze_longbow: Weapon(
            name=Weapons.bronze_longbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Weapons.bronze_crossbow: Weapon(
            name=Weapons.bronze_crossbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Weapons.bronze_byzantine_flamethrower: Weapon(
            name=Weapons.bronze_byzantine_flamethrower.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Weapons.bronze_musket: Weapon(
            name=Weapons.bronze_musket.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        #medium
        Weapons.iron_shuriken: Weapon(
            name=Weapons.iron_shuriken.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium),

        Weapons.iron_nzappa_zap: Weapon(
            name=Weapons.iron_nzappa_zap.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium),

        Weapons.iron_longbow: Weapon(
            name=Weapons.iron_longbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium),

        Weapons.iron_crossbow: Weapon(
            name=Weapons.iron_crossbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium)

        Weapons.iron_byzantine_flamethrower: Weapon(
            name=Weapons.iron_byzantine_flamethrower.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium)

        Weapons.iron_musket: Weapon(
            name=Weapons.iron_musket.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium),

        #heavy
        Weapons.steel_shuriken: Weapon(
            name=Weapons.steel_shuriken.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Weapons.steel_nzappa_zap: Weapon(
            name=Weapons.steel_nzappa_zap.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Weapons.steel_longbow: Weapon(
            name=Weapons.steel_longbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Weapons.steel_crossbow: Weapon(
            name=Weapons.steel_crossbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Weapons.steel_byzantine_flamethrower: Weapon(
            name=Weapons.steel_byzantine_flamethrower.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Weapons.steel_musket: Weapon(
            name=Weapons.steel_musket.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),
        
        #volcanic
        Weapons.volcanic_shuriken: Weapon(
            name=Weapons.volcanic_shuriken.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic),

        Weapons.volcanic_nzappa_zap: Weapon(
            name=Weapons.volcanic_nzappa_zap.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic),

        Weapons.volcanic_longbow: Weapon(
            name=Weapons.volcanic_longbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange
            finish=Finish.volcanic),

        Weapons.volcanic_crossbow: Weapon(
            name=Weapons.volcanic_crossbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic),

        Weapons.volcanic_byzantine_flamethrower: Weapon(
            name=Weapons.volcanic_byzantine_flamethrower.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic),

        Weapons.volcanic_musket: Weapon(
            name=Weapons.volcanic_musket.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic)

        