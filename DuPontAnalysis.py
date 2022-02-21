import requests 
import pandas as pd
import matplotlib.pyplot as plt


myAPIKey = '8a4cbc4ce78663879c3f56a3c0d6cf87';

stock1 = 'AAPL'

stock2 = 'DIS'

stock3 = 'UAA'

# AAPLbalanceStatements = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock2}?apikey={myAPIKey}').json()

# AAPLincomeStatements = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{stock1}?apikey={myAPIKey}').json()

# disBalance = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock2}?apikey={myAPIKey}').json()

# disIncome = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{stock2}?apikey={myAPIKey}').json()

underArmorIncome = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{stock3}?apikey={myAPIKey}').json()

underArmorBalance =  requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock3}?apikey={myAPIKey}').json()



# print(underArmorIncome[0])
# print(underArmorBalance[0])
# print("////////////////////////")
# print(disIncome[0])
# print(disIncome[1])

underArmorIncomeFiveYear = underArmorIncome[:5]
underArmorBalanceFiveYear = underArmorBalance[:5]

# AAPLtwoYearBalanceStatment = AAPLbalanceStatements[:2]
# AAPLtwoYearIncomeStatement = AAPLincomeStatements[:2]

# disTwoYearBalanceStatment = disBalance[:2]
# disTwoYearIncomeStatement = disIncome[:2]

underArmorProfitability = []
underArmorTurnOver = []
underArmorStructure = []
underArmorReturnOnEquity = []

# AAPLprofitability = []
# AAPLassetTurnOver = []
# AAPLcapitalStructure = []
# AAPLreturnOnEquity = []

years = ['2017', '2018', '2019', '2020', '2021']
# print(AAPLtwoYearIncomeStatement[0]['netIncome'])
# print(AAPLtwoYearIncomeStatement[1]['netIncome'])

for i in range(0, 5):
  profitabilityValue = underArmorIncomeFiveYear[i]['netIncome']/underArmorIncomeFiveYear[i]['revenue']
  underArmorProfitability.append(profitabilityValue)
  underArmorAssetTurnOverValue = underArmorIncomeFiveYear[i]['revenue']/underArmorBalanceFiveYear[i]['totalAssets']
  underArmorTurnOver.append(underArmorAssetTurnOverValue)
  underArmorCaptialStructureValue = underArmorBalanceFiveYear[i]['totalAssets']/underArmorBalanceFiveYear[i]['totalStockholdersEquity']
  underArmorStructure.append(underArmorCaptialStructureValue)
  underArmorReturnOnEquityValue = profitabilityValue*underArmorAssetTurnOverValue*underArmorCaptialStructureValue
  underArmorReturnOnEquity.append(underArmorReturnOnEquityValue)



# for i in range(0,2):
#   profitabilityValue = AAPLtwoYearIncomeStatement[i]['netIncome']/AAPLtwoYearIncomeStatement[i]['revenue']
#   AAPLprofitability.append(profitabilityValue)
#   assetTurnOverValue = AAPLtwoYearIncomeStatement[i]['revenue']/AAPLtwoYearBalanceStatment[i]['totalAssets']
#   AAPLassetTurnOver.append(assetTurnOverValue)
#   AAPLcapitalStructureValue = AAPLtwoYearBalanceStatment[i]['totalAssets']/AAPLtwoYearBalanceStatment[i]['totalStockholdersEquity']
#   AAPLcapitalStructure.append(AAPLcapitalStructureValue)
#   AAPLreturnOnEquityValue = profitabilityValue*assetTurnOverValue*AAPLcapitalStructureValue
#   AAPLreturnOnEquity.append(AAPLreturnOnEquityValue)
#   years.append(AAPLtwoYearBalanceStatment[i]['date'])


# print(years) 
# print(underArmorProfitability)
# print(underArmorTurnOver)
# print(underArmorStructure)
# print(underArmorReturnOnEquity)



fig, axs = plt.subplots(2,2, figsize=(8,6))
fig.suptitle('UnderArmor Stock Information')
axs[0, 0].plot(years, underArmorProfitability, color='orange')
axs[0, 1].plot(years, underArmorTurnOver, color='green')
axs[1, 0].plot(years, underArmorStructure, color='red')
axs[1, 1].plot(years, underArmorReturnOnEquity, color='blue')
axs[0,0].title.set_text('Profitability')
axs[0,1].title.set_text('Turn Over')
axs[1,0].title.set_text('Capital Structure')
axs[1,1].title.set_text('Return on Equity')


fig.tight_layout(pad=1.75)
