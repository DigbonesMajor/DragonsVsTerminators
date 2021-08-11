from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    food_cost=5
    blocks_path=False
    
    def __init__(self,armor=1):
        Dragon.__init__(self,armor)
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.4
    implemented = True  # Change to True to view in the GUI

    # END 2.4

    def action(self, colony):
        # BEGIN 2.4
        y=self.place.terminators.copy()
        for x in y:
            for i in range(len(self.place.terminators)):
                if self.place.terminators[i]==x:
                    self.place.terminators[i].reduce_armor(self.damage)
                    break
        
