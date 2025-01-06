class Creature:
    def __init__(self,initiative):
        self.initiative = initiative
        
    def get_initiative(self):
        return self.initiative
    
    def set_initiative(self,initiative):
        self.initiative = initiative