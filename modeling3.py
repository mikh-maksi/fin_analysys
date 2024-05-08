def week_calculations(week):
  week["CAC"] = week["Leads"]*week['Lead Cost']*(1+week["Sales Manager rate"])
  week["Sales"] = week["Leads"]*week['Conversion rate']
  week["LTV"] = week["LT"]*week['Average price']
  week["Incom"] = week["Sales"]*week["LTV"]
  week["Result"] = week["Incom"] - week["CAC"]
  return week



week = {
    "Name":"1-7.04",
    "Leads" : 2000,
    "Lead Cost":4000,
    "Conversion rate": 0.42,
    "Sales Manager rate":0.38,
    "CAC": 300000,
    "Sales": 3000,
    "LT":21,
    "Average price":150,
    "LTV": 3150,
    "Incom" :9450000,
    "Result": 9150000,
    "Accumulated income":None,
    "Value of investment":200000,
    "ROI":None
}
week["CAC"] = week["Leads"]*week['Lead Cost']*(1+week["Sales Manager rate"])
week["Sales"] = week["Leads"]*week['Conversion rate']
week["LTV"] = week["LT"]*week['Average price']
week["Incom"] = week["Sales"]*week["LTV"]
week["Result"] = week["Incom"] - week["CAC"]
week_time = {
    "Name": "1-7.04"
}
month_names = []
month_names.append( {"Name": "1-7.04"})
month_names.append( {"Name": "8-14.04"})
month_names.append( {"Name": "15-21.04"})
month_names.append( {"Name": "22-28.04"})
# print(month)
work_month = []
# Inputing
accumulated_income = 0
for week_name in month_names:
  week = {
    "Name":week_name,
    "Leads" : 2000,
    "Lead Cost":4000,
    "Conversion rate": 0.42,
    "Sales Manager rate":0.38,
    "CAC": 300000,
    "Sales": 3000,
    "LT":21,
    "Average price":150,
    "LTV": 3150,
    "Incom" :9450000,
    "Result": 9150000,
    "Accumulated income":None,
    "Value of investment":200000,
    "ROI":None
  }
  week = week_calculations(week)
  accumulated_income +=week["Incom"]
  week["Accumulated income"] = accumulated_income
  week["ROI"] = week["Accumulated income"]/week["Value of investment"]*100

  work_month.append(week)
# print(work_month)

# Outputing
for week_out in work_month:
  print(week_out)