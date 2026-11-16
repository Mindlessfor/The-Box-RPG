class Player:
    def __init__(self, name, sex, path):
        self.name = name
        self.sex = sex
        self.path = path[0] # path = class of the player, it increase or decrease your status based on its function

        self.level = 1
        self.cash = 10000
        
        self.life_max = 100 + path[1]
        self.life = self.life_max
        self.blood_max = 100 + path[2] # its like mana, but if it hits zero, you start to lose life
        self.blood = self.blood_max
        self.sanity_max = 100 + path[3] # sanity its based on your life, if it hits 25 percent, you start to lose defense and damage
        self.sanity = self.sanity_max
        self.fis_resistence_max = 0 + path[4] # fisical resistence
        self.fis_resistence = self.fis_resistence_max
        self.spi_resistence_max = 0 + path[5] # spiritual resistence
        self.spi_resistence = self.spi_resistence_max
        self.agility_max = 5 + path[6]
        self.agility = self.agility_max
        self.fis_damage_max = 5 + path[7] # base damage for fisical/weapon attacks
        self.fis_damage = self.fis_damage_max
        self.spi_damage_max = 5 + path[8] # base additional damage to spiritual attacks
        self.spi_damage = self.spi_damage_max

        self.domain = path[9] # some types of attacks/rituals get buffed if its on its domain type

        inventory = {}
