import random

# Supply: Random number of stones mined between 1 and 100
stonesNumber = random.randint(1, 100)

# Mining cost per stone (supply cost) with random variation between 4 and 30 anas
stonesMiningCost = random.randint(4, 30)
companyMiningCost = stonesNumber * stonesMiningCost

# Demand: Chance of a stone being sold (between 35% and 100%)
demandRate = round(random.random() * 0.8 + 0.35, 2) 
if demandRate > 0.98:
    demandRate = 0.98
    
# Markup on the stones (fixed cost added to mining cost)
stonesMarkup = round(stonesMiningCost / random.randint(2, 5))
stonesCost = stonesMarkup + stonesMiningCost

# Number of stones sold based on supply (stonesNumber) and demand rate
stonesSold = int(stonesNumber * demandRate)

companySales = stonesCost * stonesSold
companyProfit = companySales - companyMiningCost

print("There were", stonesNumber, "stones mined, each at a cost of", stonesMiningCost, "anas, and at a total cost of",
      companyMiningCost, "anas.")
print("The company adds a markup of", stonesMarkup, "anas, for a sale price of", stonesCost, "anas.")
print("Out of the", stonesNumber, "stones,", stonesSold, "stones were sold, for a total sales of", companySales, "anas.")
if demandRate > 0.95:
    print("People really want these stones! Demandm was at a rate of",demandRate*100,"% today.")
else:
    print("Demand was at a rate of",demandRate*100,"% today.")
if companyProfit < 0:
    print("Sales were bad. The company lost", companyProfit * -1, "anas.")
elif 0 < companyProfit < companyMiningCost * 1.25:
    print("Sales were okay. The company made", companyProfit, "anas.")
else:
    print("Business is booming! The company made", companyProfit, "anas.")
