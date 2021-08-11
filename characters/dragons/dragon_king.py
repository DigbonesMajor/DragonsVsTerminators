from characters.dragons.scuba_thrower import ScubaThrower
from .dragon import Dragon
from utils import terminators_win


class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True  # Change to True to view in the GUI
    food_cost=7
    instantiated=False


    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        ScubaThrower.__init__(self,armor)
        self.fake=DragonKing.instantiated
        DragonKing.instantiated=True
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if self.fake==True:
            self.reduce_armor(self.armor)
        else:
            temp=self.place.exit
            while temp!=None:
                if temp.dragon != None:
                    if temp.dragon.is_container:
                        if temp.dragon.contained_dragon!=None and temp.dragon.contained_dragon.is_buffed ==False:
                            temp.dragon.contained_dragon.damage= 2*temp.dragon.contained_dragon.damage
                            temp.dragon.contained_dragon.is_buffed=True 
                    if temp.dragon.is_buffed==False:
                        temp.dragon.damage=2*temp.dragon.damage
                        temp.dragon.is_buffed= True 
                temp=temp.exit 
            super().action(colony)
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        self.armor-=amount
        if self.armor<=0 and self.fake==False:
            terminators_win()
        elif self.fake==True:
            self.place.remove_fighter(self)
            self.death_callback()

