from .dragon import Dragon


class BodyguardDragon(Dragon):
    """BodyguardDragon provides protection to other Dragons."""

    name = 'Bodyguard'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.2
    food_cost=4 
    is_container=True
    implemented = True# Change to True to view in the GUI

    def __init__(self, armor=2):
        Dragon.__init__(self, armor)
        self.contained_dragon = None  # The Dragon hidden in this bodyguard

    def can_contain(self, other):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        if self.contained_dragon!= None or other.is_container==True:
            return False
        else:
            return True 
        # END 3.2

    def contain_dragon(self, dragon):
        # BEGIN 3.2
        if self.can_contain(dragon):
            self.contained_dragon=dragon 
	
        
        # END 3.2

    def action(self, colony):
        # BEGIN 3.2
        if self.contained_dragon is not None:
            self.contained_dragon.action(colony)
        # END 3.2
