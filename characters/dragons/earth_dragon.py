from .dragon import Dragon 
class EarthDragon(Dragon):
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost=4 
    name='Earth'
    implemented=True 
    def __init__(self,armor=4):
        Dragon.__init__(self,armor)
