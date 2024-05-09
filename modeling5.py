import numpy as np
month = []
Leads=np.random.normal(100,0,4)
LeadCost=np.random.normal(95,25,4)
ConversionRate=np.random.normal(0.32,0.015,4)
SalesManagerRate=np.random.normal(0.05,0,4)
LT=np.random.normal(3,0,4)
AP=np.random.normal(150,37.5,4)
for i in range(len(Leads)):
  week = []
  week.append(round(Leads[i]))
  week.append(round(LeadCost[i]))
  week.append(round(ConversionRate[i],2))
  week.append(round(SalesManagerRate[i],2))
  week.append(round(LT[i]))
  week.append(round(AP[i]))
  month.append(week)
print(month)