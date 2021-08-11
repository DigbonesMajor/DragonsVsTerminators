from .dragon import Dragon


class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.3
    food_cost=4 
    time_to_digest=3
    implemented = True  # Change to True to view in the GUI

    # END 2.3

    def __init__(self, armor=1):
        # BEGIN 2.3
        Dragon.__init__(self, armor)
        self.digesting=0
        "*** YOUR CODE HERE ***"
        # END 2.3

    def eat_terminator(self, terminator):
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
        # END 2.3

    def action(self, colony):
        # BEGIN 2.3
        if self.digesting>0:
            self.digesting-=1 
        else:
            doing=0
            if len(self.place.terminators)>0:
                doing+=1 
                self.place.terminators[0].reduce_armor(self.place.terminators[0].armor)
            if doing>0:
                self.digesting=self.time_to_digest
        "*** YOUR CODE HERE ***"
