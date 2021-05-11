

import requests
import bs4

#Url used to gather prices on ores
result = requests.get("https://oldschool.runescape.wiki/w/Mining")
soup = bs4.BeautifulSoup(result.text,'lxml')

#the following 5 functions pull the prices of each ore

def coal_price():
    coaltext = soup.select('.coins')[20]
    coalp = (coaltext.text)
    coalp = int(coalp.replace(',',''))
    return coalp

def gold_price():
    goldtext = soup.select('.coins')[21]
    goldp = goldtext.text
    goldp = int(goldp.replace(',',''))
    return goldp


def mith_price():
    mithtext = soup.select('.coins')[22]
    mithp = mithtext.text
    mithp = int(mithp.replace(',',''))
    return mithp

def addy_price():
    addytext = soup.select('.coins')[23]
    addyp = addytext.text
    addyp = int(addyp.replace(',',''))
    return addyp

def rune_price():
    runetext = soup.select('.coins')[25]
    runep = runetext.text
    runep = int(runep.replace(',',''))
    return runep

#Stores the results of prices
coalprice = coal_price()
goldprice = gold_price()
mithprice = mith_price()
addyprice = addy_price()
runeprice = rune_price()


#prints out all of the ores prices
def ore_prices():
    print(f"Coal:\t{coalprice}gp")
    print(f"Gold:\t{goldprice}gp")
    print(f"Mith:\t{mithprice}gp")
    print(f"Addy:\t{addyprice}gp")
    print(f"Rune:\t{runeprice}gp")


#figures out how much coal is needed
def coal_needed(gold,coal,mith,addy,rune):
    
    coalneed = (mith*2) + (addy*3) + (rune*4) - coal + (gold*0)
    coalneed = int(coalneed)
    return coalneed
    

#calculates the cost of the coal needed by the coal price
def coal_cost(gold,coal,mith,addy,rune):
    coalneed = (mith*2) + (addy*3) + (rune*4) - coal + (gold*0)
    coalneed = int(coalneed)
    return coalprice*coalneed

#total profit if selling all ores
def ore_profit(gold,coal,mith,addy,rune):
    
    mprof = mith * mithprice
    aprof = addy * addyprice
    rprof = rune * runeprice
    cprof = coal * coalprice
    gprof = gold * goldprice
    total = mprof + aprof + rprof + cprof + gprof
    return total


#this grabs the url for the bar prices
result2 = requests.get('https://oldschool.runescape.wiki/w/Smithing')
soup2 = bs4.BeautifulSoup(result2.text,'lxml')

#the following 4 functions grab the bar prices

def gold_bar():
    gbtext = soup2.select('.coins')[15]
    gbar = int(gbtext.text)
    return gbar

def mith_bar():
    mbtext = soup2.select('.coins')[18]
    mbar = int(mbtext.text)
    return mbar

def addy_bar():
    abtext = soup2.select('.coins')[21]
    abar = abtext.text
    abar = int(abar.replace(',',''))
    return abar

def rune_bar():
    rbtext = soup2.select('.coins')[24]
    rbar = rbtext.text
    rbar = int(rbar.replace(',',''))
    return rbar

#stores the values
gbar = gold_bar()
mbar = mith_bar()
abar = addy_bar()
rbar = rune_bar()

#prints out all of the bar prices
def bar_prices():
    print(f"Gold:\t{gbar}gp")
    print(f"Mith:\t{mbar}gp")
    print(f"Addy:\t{abar}gp")
    print(f"Rune:\t{rbar}gp")



#calculates how much profit if user decides to smith ores into bars
#this includes smithing gold bars
def bar_profit_wg(gold,coal,mith,addy,rune):
    
    gbprof = (gbar*gold)
    mbprof = (mbar*mith)
    abprof = (abar*addy)
    rbprof = (rbar*rune)
    coalcost = coal_cost(gold,coal,mith,addy,rune)
    ore_prof = ore_profit(gold,coal,mith,addy,rune)
    bprofga = gbprof + mbprof + abprof + rbprof - coalcost - ore_prof
    bprofg = gbprof + mbprof + abprof + rbprof - coalcost
    
    print(f"Coal cost:{coalcost}")
    print(f"Smithing Profit: {bprofga}")
    print(f"Total Profit: {bprofg}")
    




#calculates how much profit if user decides to smith ores into bars
#this doesn't include smithing gold bars
def bar_profit_ng(gold,coal,mith,addy,rune):
    #additional profit if turning ores into bars
    #doesn't include smelting gold bars
    
    #bar profit = (Bar price)*ores - (coalprice times * coal needed to make bar)*ores - (ore price)*ores
    gbprof = 2*(gold_price()*gold)
    mbprof = (mbar*mith)
    abprof = (abar*addy)
    rbprof = (rbar*rune)
    coalcost = coal_cost(gold,coal,mith,addy,rune)
    ore_prof = ore_profit(gold,coal,mith,addy,rune)
    bprofa = mbprof + abprof + rbprof - coalcost - ore_prof +gbprof
    bprof = mbprof + abprof + rbprof - coalcost + gbprof
    
    print(f"Coal cost:{coalcost}")
    print(f"Smithing Profit: {bprofa}")
    print(f"Total Profit: {bprof}")



import time

#This function allows the user to start an automated prompt

def ore_func():
    
    #start up section
    #will ask user for ore input
    print("Starting up...")
    time.sleep(1)
    print("Welcome to OSRS Ore Calc")
    time.sleep(1)
    print("To get started, please fill out some info")
    
    #This collects the information needed to do any of the calculations
    gold = int(input("Gold Ores: "))
    coal = int(input("Coal Ores: "))
    mith = int(input("Mith Ores: "))
    addy = int(input("Addy Ores: "))
    rune = int(input("Rune Ores: "))
    
    print("\n")
    
    #stores input into a list and unpacks them into
    orelist = (gold,coal,mith,addy,rune)
    oreprofit = ore_profit(*orelist)
    print('\n')
    print("Thank you\n")
    time.sleep(1)
    
    while True: 
        #available functions
        print("Functions:")
        print("1. Ore Prices")
        print("2. Bar Prices")
        print("3. Coal Needed")
        print("4. Ore Profit")
        print("5. Bar Profit w/ smithing Gold")
        print("6. Bar Profit w/o smithing Gold")
        print("E. Exit\n")
        
        #allows user to pick their choice
        choice = input("Please select a function: 1/2/3/4/5/6/E: \n")
        
        #takes input and applies it to a function
        if choice in ('1','2','3','4','5','6'):
            
            if choice == '1':
                print('\nRetrieving ore prices...\n')
                time.sleep(1)
                ore_prices()
                print('\n')
                
            elif choice == '2':
                print('\nRetrieving bar prices...\n')
                time.sleep(1)
                bar_prices()
                print('\n')
            
            elif choice == '3':
                print('\nCalculating...\n')
                time.sleep(1)
                print(f"To smith all ores you'll need {coal_needed(*orelist)} more coal")
                print(f"The cost of the extra coal would be: {coal_cost(*orelist)}gp")
                print('\n')
                               
            elif choice == '4':
                print('\nCalculating...\n')
                time.sleep(1)
                print(f"Ore Profit:\t{oreprofit}")
                
                print('\n')
            elif choice == '5':
                print('\nCalculating...\n')
                time.sleep(1)
                bar_profit_wg(*orelist)
                print('\n')
            elif choice == '6':
                print('\nCalculating...\n')
                time.sleep(1)
                bar_profit_ng(*orelist)
                print('\n')
                
                
        #exits the function       
        elif choice == 'e' or choice == 'E' or choice == 'exit' or choice == 'Exit'or choice == '7':
            print("\nThanks for using the calculator\n")
            print("Shutting down.....")
            time.sleep(1)
            break
        
        #lets the user know they picked an invalid choice
        else:
            print("Please enter a valid choice\n")



