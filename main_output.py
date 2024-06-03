import random

stonesNumber = random.randint(1,100)
stonesMiningCost = random.randint(4,30)
companyMiningCost = stonesNumber*stonesMiningCost
stonesMarkup = round(stonesMiningCost/random.randint(2,5))
stonesCost = stonesMarkup + stonesMiningCost
stonesSold = random.randint(4,stonesMiningCost)
companySales = stonesCost*stonesSold
companyProfit = companySales - companyMiningCost

print("There were",stonesNumber,"stones mined, each at a cost of",stonesMiningCost,"anas, and at a total cost of",companyMiningCost,"anas.")
print("The company adds a markup of",stonesMarkup,"anas, for a sale price of",stonesCost,"anas.")
print("Out of the",stonesNumber,"stones,",stonesSold,"stones were sold, for a total sales of",companySales,"anas.")
if companyProfit < 0:
    print("Sales were bad. The company lost",companyProfit*-1,"anas.")
elif 0 < companyProfit < companyMiningCost*1.5:
    print("Sales were okay. The company made",companyProfit,"anas.")
else:
    print("Business is booming! The company made",companyProfit,"anas.")
