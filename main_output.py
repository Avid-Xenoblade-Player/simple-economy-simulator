import random

stonesNumber = random.randint(1,100)
stonesMiningCost = random.randint(4,30)
companyMiningCost = stonesNumber*stonesMiningCost
stonesMarkup = stonesMiningCost/random.randint(2,5)
stonesCost = stonesMarkup + stonesMiningCost
stonesSold = random.randint(4,stonesMiningCost)
companySales = stonesCost*stonesSold
companyProfit = companySales-companyMiningCost
