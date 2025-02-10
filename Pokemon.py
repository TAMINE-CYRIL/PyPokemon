class Pokemon:
    def __init__(self, name, ptype, hp, attack, defense, speed, level):
        self.name = name
        self.ptype = ptype
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(self.name, "is KO!")


