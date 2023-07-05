class Ankara:
    def __init__(self,mood,temperature):
        self.mood=mood
        self.temperature=temperature
    def get_partern(self):
        # moods=range(1,5)
        # temp=range(20,30)
        if self.temperature >=20  and self.mood >=5:
            return f"wear light coloured and heavy ankara"
        else:
            return f"wear dull and light ankara"
ankara=Ankara(23,5)
print(ankara.get_partern())

class Migration:
    def __init__(self,weather,river_level,predator_locations,species,location):
        self.weather=weather
        self.river_level=river_level
        self.predator_locations=predator_locations
        self.species=species
        self.location=location
    def get_movement(self):
        if self.weather=="dry" and self.river_level=="low" and self.predator_locations=="near" and self.location=="Mara":
         return f"{self.species} will migrate  to {self.location}"
        else:
            return f"{self.species} will not migrate to {self.location} "
        
migration=Migration("dry", "low","near","wildbeast","Mara")
print(migration.get_movement())

class Nollywood:
    def __init__(self,shooting_schedules,budgets,cast):
        self.shooting_schedules=shooting_schedules
        self.cast=cast
        self.budgets=budgets
    def all_budgets(self):
        if self.shooting_schedules==range(2,7) and self.cast>=10 and self.budgets==10000000:
            return f"if {self.cast} casts are shooting a movie at {self.shooting_schedules}pm then the budjet will be {self.budgets} will be high"
        else:
            return f"if {self.cast} casts are shooting a movie at {self.shooting_schedules}pm then the budget will below {self.budgets}"
nollywood=Nollywood(6,90000,3)
print(nollywood.all_budgets())

class Fruit:
    def __init__(self,fruit_type,fruit_power,power_pose,fruit_effect):
        self.fruit_type=fruit_type
        self.fruit_power=fruit_power
        self.power_pose=power_pose
        self.fruit_effect=fruit_effect
    def get_fruit(self):
        if self.fruit_type=="apple" and self.fruit_power >=10 and self.power_pose=="strong" and self.fruit_effect=="good":
            return f"{self.fruit_type} is a fruit that has power lots of power of {self.fruit_power} and it poses {self.power_pose} power it has {self.fruit_effect} effect"
        else:
            return f"{self.fruit_type} is fruit that has little of power {self.fruit_power}  and it poses {self.power_pose} power it has {self.fruit_effect} effect"
fruit=Fruit("mango",7,"weak","bad")
print(fruit.get_fruit())




class Nollywood:
    def __init__(self,name_film,cast,schedule,location,budjet):
        self.name_film=name_film
        self.cast=cast
        self.schedule=schedule
        self.budjet=budjet
        self.location=location
    def plan_movie(self):
        return f"{self.name_film} will have the following casts {self.cast} and will be shoot on {self.schedule}  at {self.location} giving it a budjet of {self.budjet}"

nollywood=Nollywood("Cinderella",("John Doe","Mary Sinachi","Mercy Mbone"),("24-05-2023","10.00AM to 12.00AM"), "Abuja","$10000")
print (nollywood.plan_movie())     
      
        
        
            
        
        
        
        
        
        
        
        