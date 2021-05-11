
#Creates a class that figures out "effective strength"
#This class will later convert the inputs into values for calculating
class Strength:
    
    def __init__(self,strl,potb,pryb,othb,styb,strb):
        
        self.strl = strl
        self.potb = potb
        self.pryb = pryb
        self.othb = othb
        self.styb = styb
        self.strb = strb
    
    #gives the potion bonus
    def potion_bonus(self):
    
        if self.potb == 1:
            return 0
        
        elif self.potb == 2:
            return 3+(.10*self.strl)
        
        elif self.potb == 3:
            return 5+(.15*self.strl)
        
        elif self.potb == 4:
            return 2+(.12*self.strl)
        
        else:
            print("incorrect number")
    
    #gives the prayer bonus
    def prayer_bonus(self):
        
        if self.pryb == 1:
            return 1
        
        elif self.pryb == 2:
            return 1.05
        
        elif self.pryb == 3:
            return 1.1
        
        elif self.pryb == 4:
            return 1.15
        
        elif self.pryb == 5:
            return 1.18
        
        elif self.pryb == 6:
            return 1.23
        
        else:
            print("incorrect number")
     
    #gives the armor set bonus
    def set_bonus(self):
        
        if self.othb == 1:
            return 1
        
        elif self.othb == 2:
            return 1.05
        
        elif self.othb == 3:
            return 1.16*(7/6)
        
        elif self.othb == 4:
            return 1.15
        
        elif self.othb == 5:
            return 1.2
        
        elif self.othb == 6:
            return 1.025

        else:
            print("incorrect number")
    
    #gives the bonus based on attack style
    def style_bonus(self):
        
        if self.styb == 1:
            return 3
        
        elif self.styb == 2:
            return 1
        
        elif self.styb == 3:
            return 0
        
        else:
            print("incorrect number")
            
#This calculates the modifier for a specific armor set
def dharok_mod(x):
    #x is max hp
    #y is current hp
    dam_mod = 1 + (((x-1)/100)*(x/100))
    return float(dam_mod)


#the function that calculates damage
def base_damage(x,y):
    #x is effective str
    #y is strength bonus
    
    basedamage = float(1.3 + (x/10) + (y/80) + ((x*y)/640))
    return basedamage
    


#this function allows the user to add the necessary inputs to get the calculation
def damage_calculator():
    
    strength = int(input("Strength level: "))
    potion = int(input("Potions:\n1.None\n2.Strength Potion\n3.Super Strength/Overload\n4.Zammy Brew\n5.Dragon Battleaxe special\nPotion 1/2/3/4/5: "))
    prayer = int(input("\nPrayers:\n1.None\n2.Burst of Strength 5%\n3.Superhuman Strength 10%\n4.Ultimate Strength 15%\n5.Chivalry 18%\n6.Piety 23%\nChoose Prayer: "))
    setbon = int(input("\nSet Bonuses:\n1.None/Dharok's\n2.Void\n3.Slayer Helm\n4.Salve Amulet\n5.Salve Amulet(e)\n6.Inquisitor's Armour\nSet bonus 1/2/3/4/5/6: "))
    style = int(input("\nAttack Style:\n1.Aggressive\n2.Controlled\n3.Accurate/Defensive\nAttack style: "))
    strbon = int(input("\nStrength Bonus: "))
    if setbon == 1:
        dhar = input("\nDharok Set?Y/N: ")
    else:
        dhar = 0
    print('\n')
    
    #stores the inputs into a list
    stats = [strength,potion,prayer,setbon,style,strbon]
    #unpacks the list to convert user input into class values
    stats1 = Strength(*stats)
    
    #asks for an extra input if the user wants to use the Dharok armor set bonus
    if dhar == 'y' or dhar == 'Y' or dhar == 'yes' or dhar == 'Yes':
        hp = float(input("Max HP level?: "))
        modifier = dharok_mod(hp)
        modify = float(modifier)

    else:
        pass

    
    #calculates the effective strength based on the user's inputs
    def effstr():
        strength1 = stats1.strl
        potion1 = stats1.potion_bonus()
        prayer1 = stats1.prayer_bonus()
        setbonus1 = stats1.set_bonus()
        style1 = stats1.style_bonus()

        return ((strength1+potion1)*prayer1*setbonus1)+style
        
    effstrength = effstr()
    print('\n')
    
    #lets user know max damage with and without Dharok armor set
    if dhar == 'y' or dhar == 'Y' or dhar == 'yes' or dhar == 'Yes':
        max_hit = base_damage(effstrength,strbon)
        print(f"Max hit without DH:{max_hit}")
        dhmax = max_hit*modify
        print(f"Max hit with DH:{dhmax}")

        
    #lets user know max damage without Dharok armor set
    elif dhar == 'n' or dhar == 'N' or dhar == 'no' or dhar == 'No' or dhar == 0:
        
        max_hit = base_damage(effstrength,strbon)
        print(f"Max hit:{max_hit}")
        

