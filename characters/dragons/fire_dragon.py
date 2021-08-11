from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    damage = 3
    food_cost=5 
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.2
    
    implemented = True   # Change to True to view in the GUI

    # END 2.2

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Make sure to damage each terminator in the current place, and apply the bonus
        if the fire dragon dies.
        """
        # BEGIN 2.2
        self.armor -= amount
        y=self.place.terminators.copy()
        for x in y:
            for i in range(len(self.place.terminators)):
                if self.place.terminators[i]==x:
                    self.place.terminators[i].reduce_armor(amount)
                    break
    
        if self.armor <= 0:
            y=self.place.terminators.copy()
            for x in y:
                for i in range(len(self.place.terminators)):
                    if self.place.terminators[i]==x:
                        self.place.terminators[i].reduce_armor(self.damage)
                        break
        
            
            self.place.remove_fighter(self)
            self.death_callback()
    