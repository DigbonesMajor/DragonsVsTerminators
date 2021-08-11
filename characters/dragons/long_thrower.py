from .thrower_dragon import ThrowerDragon


class LongThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at least 5 places away."""

    name = 'Long'
    # OVERRIDE CLASS ATTRIBUTES HERE 2.1 
    food_cost=2
    implemented = True  # Change to True to view in the GUI
    min_range=5
    max_range=float('inf')
    # END 2.1
