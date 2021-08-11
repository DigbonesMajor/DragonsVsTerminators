from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.5
    implemented = True  # Change to True to view in the GUI
    

    # END 4.5

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
        # BEGIN 4.5
        temp={}
        distance=0
        while self.place.name!='Skynet':
            for x in self.place.terminators:
                temp[x]=distance
            if self.place.dragon is not None:
                if self.place.dragon.is_container:
                    temp[self.place.dragon]=distance
                    if self.place.dragon.contained_dragon !=None and distance!=0:
                        temp[self.place.dragon.contained_dragon]=distance
                elif distance!=0:
                    temp[self.place.dragon]=distance
            self.place=self.place.entrance
            distance+=1
        return temp  
        # END 4.5

    def calculate_damage(self, distance):
        # BEGIN 4.5
        base_damage=2-0.2*distance - 0.05*self.fighters_shot
        if base_damage>0:
            return base_damage
        else:
            return 0

        # END 4.5

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
