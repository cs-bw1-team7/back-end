from enum import auto
from .named_enum import NamedEnum
from .equipment import (Weapon, Style, Finish, Style_Description, Finish_Description)

class Items(NamedEnum):
    '''
    ===Overview===
    The Items class handles the weapon generation and each weapon will have attributes for style and finish.
    
    ===Attributes===
    name: This attribute gives the weapon a str type name
    
    style_description: This attribute is a str that describes the style type associated with that weapon for players to inspect the item.
    
    finish_description: This attribute is a str that describes the finish type associated with that weapon for players to inspect the item.
    
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

    '''
    Substitute " _ " with " " for item name
    '''

    #melee Items (close range combat)
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
    
    #midrange Items(midrange combat)
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

    #projectile Items(long range combat)

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
        Items.bronze_wrist_blades: Weapon(
            name=Items.bronze_wrist_blades.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),
        
        Items.bronze_knuckles: Weapon(
            name=Items.bronze_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Items.bronze_knife: Weapon(
            name=Items.bronze.knife.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Items.bronze_viking_halberd: Weapon(
            name=Items.bronze_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Items.bronze_rondel_dagger: Weapon(
            name=Items.bronze_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Items.bronze_war_hammer: Weapon(
            name=Items.war_hammer.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),

        Items.bronze_whipping_chain: Weapon(
            name=Items.whipping_chain.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.light,
            style=Style.melee,
            finish=Finish.light),
        
        #medium
        Items.iron_wrist_blades: Weapon(
            name=Items.iron_wrist_blades.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Items.iron_knuckles: Weapon(
            name=Items.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Items.iron_knife: Weapon(
            name=Items.iron_knife.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Items.iron_viking_halberd: Weapon(
            name=Items.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Items.iron_rondel_dagger: Weapon(
            name=Items.iron_rondel_dagger.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Items.iron_war_hammer: Weapon(
            name=Items.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        Items.iron_whipping_chain: Weapon(
            name=Items.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.medium,
            style=Style.melee,
            finish=Finish.medium),

        #heavy
        Items.steel_wrist_blades: Weapon(
            name=Items.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Items.steel_knuckles: Weapon(
            name=Items.steel_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Items.steel_knife: Weapon(
            name=Items.steel_knife.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Items.steel_viking_halberd: Weapon(
            name=Items.steel_viking_halberd.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Items.steel_rondel_dagger: Weapon(
            name=Items.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Items.steel_war_hammer: Weapon(
            name=Items.steel_war_hammer.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        Items.steel_whipping_chain: Weapon(
            name=Items.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.heavy,
            style=Style.melee,
            finish=Finish.heavy),

        #volcanic
        Items.volcanic_wrist_blades: Weapon(
            name=Items.volcanic_wrist_blades.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Items.volcanic_knuckles: Weapon(
            name=Items.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Items.volcanic_knife: Weapon(
            name=Items.volcanic_knife.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Items.volcanic_viking_halberd: Weapon(
            name=Items.volcanic_viking_halberd.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Items.volcanic_rondel_dagger: Weapon(
            name=Items.volcanic_rondel_dagger.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),
        
        Items.volcanic_war_hammer: Weapon(
            name=Items.volcanic_war_hammer.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),

        Items.volcanic_whipping_chain: Weapon(
            name=Items.iron_knuckles.name,
            style_description=Style_Description.melee,
            finish_description=Finish_Description.volcanic,
            style=Style.melee,
            finish=Finish.volcanic),
        
        #midrange
        #light
        Items.bronze_arming_sword: Weapon(
            name=Items.bronze_arming_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Items.bronze_estoc: Weapon(
            name=Items.bronze_estoc.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),
        
        Items.bronze_katana: Weapon(
            name=Items.bronze_katana.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Items.bronze_long_sword: Weapon(
            name=Items.bronze_long_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Items.bronze_rapier: Weapon(
            name=Items.bronze_rapier.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Items.bronze_chain: Weapon(
            name=Items.bronze_chain.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),

        Items.bronze_morning_star: Weapon(
            name=Items.bronze_morning_star.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.light,
            style=Style.midrange,
            finish=Finish.light),
        
        #medium
        Items.iron_arming_sword: Weapon(
            name=Items.iron_arming_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Items.iron_estoc: Weapon(
            name=Items.iron_estoc.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Items.iron_katana: Weapon(
            name=Items.bronze_katana.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.light),

        Items.iron_long_sword: Weapon(
            name=Items.iron_long_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Items.iron_rapier: Weapon(
            name=Items.iron_rapier.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Items.iron_chain: Weapon(
            name=Items.iron_chain.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),

        Items.iron_morning_star: Weapon(
            name=Items.iron_morning_star.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.medium,
            style=Style.midrange,
            finish=Finish.medium),
        
        #heavy
        Items.steel_arming_sword: Weapon(
            name=Items.steel_arming_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Items.steel_estoc: Weapon(
            name=Items.steel_estoc.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Items.steel_katana: Weapon(
            name=Items.bronze_katana.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Items.steel_long_sword: Weapon(
            name=Items.steel_long_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Items.steel_rapier: Weapon(
            name=Items.steel_rapier.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Items.steel_chain: Weapon(
            name=Items.steel_chain.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),

        Items.steel_morning_star: Weapon(
            name=Items.steel_morning_star.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.heavy,
            style=Style.midrange,
            finish=Finish.heavy),
        
        #volcanic
        Items.volcanic_arming_sword: Weapon(
            name=Items.volcanic_arming_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Items.volcanic_estoc: Weapon(
            name=Items.volcanic_estoc.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Items.volcanic_katana: Weapon(
            name=Items.bronze_katana.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Items.volcanic_long_sword: Weapon(
            name=Items.volcanic_long_sword.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Items.volcanic_rapier: Weapon(
            name=Items.volcanic_rapier.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Items.volcanic_chain: Weapon(
            name=Items.volcanic_chain.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),

        Items.volcanic_morning_star: Weapon(
            name=Items.volcanic_morning_star.name,
            style_description=Style_Description.midrange,
            finish_description=Finish_Description.volcanic,
            style=Style.midrange,
            finish=Finish.volcanic),
        
        #longrange
        #light
        Items.bronze_shuriken: Weapon(
            name=Items.bronze_shuriken.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Items.bronze_nzappa_zap: Weapon(
            name=Items.bronze_nzappa_zap.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Items.bronze_longbow: Weapon(
            name=Items.bronze_longbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Items.bronze_crossbow: Weapon(
            name=Items.bronze_crossbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Items.bronze_byzantine_flamethrower: Weapon(
            name=Items.bronze_byzantine_flamethrower.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        Items.bronze_musket: Weapon(
            name=Items.bronze_musket.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.light,
            style=Style.longrange,
            finish=Finish.light),

        #medium
        Items.iron_shuriken: Weapon(
            name=Items.iron_shuriken.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium),

        Items.iron_nzappa_zap: Weapon(
            name=Items.iron_nzappa_zap.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium),

        Items.iron_longbow: Weapon(
            name=Items.iron_longbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium),

        Items.iron_crossbow: Weapon(
            name=Items.iron_crossbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium)

        Items.iron_byzantine_flamethrower: Weapon(
            name=Items.iron_byzantine_flamethrower.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium)

        Items.iron_musket: Weapon(
            name=Items.iron_musket.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.medium,
            style=Style.longrange,
            finish=Finish.medium),

        #heavy
        Items.steel_shuriken: Weapon(
            name=Items.steel_shuriken.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Items.steel_nzappa_zap: Weapon(
            name=Items.steel_nzappa_zap.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Items.steel_longbow: Weapon(
            name=Items.steel_longbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Items.steel_crossbow: Weapon(
            name=Items.steel_crossbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Items.steel_byzantine_flamethrower: Weapon(
            name=Items.steel_byzantine_flamethrower.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),

        Items.steel_musket: Weapon(
            name=Items.steel_musket.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.heavy,
            style=Style.longrange,
            finish=Finish.heavy),
        
        #volcanic
        Items.volcanic_shuriken: Weapon(
            name=Items.volcanic_shuriken.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic),

        Items.volcanic_nzappa_zap: Weapon(
            name=Items.volcanic_nzappa_zap.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic),

        Items.volcanic_longbow: Weapon(
            name=Items.volcanic_longbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange
            finish=Finish.volcanic),

        Items.volcanic_crossbow: Weapon(
            name=Items.volcanic_crossbow.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic),

        Items.volcanic_byzantine_flamethrower: Weapon(
            name=Items.volcanic_byzantine_flamethrower.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic),

        Items.volcanic_musket: Weapon(
            name=Items.volcanic_musket.name,
            style_description=Style_Description.longrange,
            finish_description=Finish_Description.volcanic,
            style=Style.longrange,
            finish=Finish.volcanic)
    }
        