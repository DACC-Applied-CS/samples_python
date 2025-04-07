class Character:
    def __init__(self, name, health, stamina, level):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.level = level

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Stamina: {self.stamina}, Level: {self.level}"
    
class NPC(Character):
    def __init__(self, name, health, stamina, level, allegiance, aggression):
        super().__init__(name, health, stamina, level)
        self.allegiance = allegiance
        self.aggression = aggression

    def __str__(self):
        return super().__str__() + f"\nAllegiance to: {self.allegiance}, Aggression level of: {self.aggression}"

class NPCInteractive(NPC):
    def __init__(self, name, health, stamina, level, allegiance, aggression, goods_traded, quest_info):
        super().__init__(name, health, stamina, level, allegiance, aggression)
        self.goods_traded = goods_traded
        self.quest_info = quest_info

    def __str__(self):
        return super().__str__() + f"\nGoods traded: {self.goods_traded}, Quest info: {self.quest_info}"

class MainCharacter(Character):
    def __init__(self, name, health, stamina, level, reputation, money):
        super().__init__(name, health, stamina, level)
        self.reputation = reputation
        self.money = money

    def __str__(self):
        return super().__str__() + f"\nReputation: {self.reputation}, Remaining money: {self.money}"
    
    def make_purchase(self, amount):
        if self.money >= amount:
            self.money -= amount
            print(f"Purchased item for {amount}. Remaining money: {self.money}")
        else:
            print("Not enough money to make the purchase.")

def main():
    print('\033c\n')
    npc = NPC(name="Dutch Van Der Linde", health=80, stamina=80, level=5, allegiance="Van Der Linde Gang", aggression=60)
    print(npc)
    print()

    npc_interactive = NPCInteractive(name="Hosea Matthews", health=85, stamina=85, level=7, allegiance="Van Der Linde Gang", aggression=40, goods_traded="maps", quest_info="Bank Robbery")
    print(npc_interactive)    
    print()

    main_char = MainCharacter(name="Arthur Morgan", health=100, stamina=100, level=10, reputation="Hero", money=1500)
    print(main_char)
    print()

    main_char.make_purchase(500)

    players = [npc, npc_interactive, main_char]

    for player in players:
        print()
        print(player)
        print(type(player))
        print("Character?", isinstance(player, Character))
        print("NPC?", isinstance(player, NPC))
        print("NPC Interactive?", isinstance(player, NPCInteractive))
        print("Main Character?", isinstance(player, MainCharacter))

main()