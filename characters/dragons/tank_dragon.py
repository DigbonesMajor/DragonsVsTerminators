from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    food_cost=6
    implemented = True  # Change to True to view in the GUI
    armor=2
        

    # END 3.3

    def action(self, colony):
        # BEGIN 3.3
        if self.contained_dragon!=None:
            self.contained_dragon.action(colony)
        y=self.place.terminators.copy()
        for x in y:
            for i in range(len(self.place.terminators)):
                if self.place.terminators[i]==x:
                    self.place.terminators[i].reduce_armor(self.damage)
                    break
            
