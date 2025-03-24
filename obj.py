class Player:
    pass    

p1=Player()
p2=Player()
print(type(p1))
print(type(p2))

class Player:
 def __init__(self,gender,health,name,defaultWeapon,credits):
    self.gender=gender
    self.health=health
    self.name=name
    self.defaultWeapon=defaultWeapon
    self.credits=credits

p1=Player(100, "F")
p2=Player(90, "M")

print(p1.health)
print(p1.gender)
print(p2.health)
print(p2.gender)

p1.health=200
p2.health=p2.health-40
print(p1.health)
print(p2.health) 

def playerHurt(self,damage):
        self.health=self.health-damage
        print("Damage=",damage,"New Health=",self.health)

p1=Player("F",110)
p2=Player("M",100)
p1.playerHurt(20)
p2.playerHurt(10.5)

def isDead(self):
    if self.health<=0:
        return True
    else 
        return False
    
p1=Player(100,"F")
p2=Player(90,"M")
print(p1.isDead())
print(p2.isDead())
