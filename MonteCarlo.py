import pandas as pd
import matplotlib.pyplot as plt
import random
from statistics import mean

df = pd.read_csv("SSO.csv")
df = df[["Date","SSO","SPY","SSO Return","SPY Return"]]
df.dropna(inplace=True)

df['SSO Return'] = df["SSO Return"].apply(lambda x: float(x.strip("%"))/100)

trading_days = 252
years = 10
total_trading_days = trading_days * years

def MonteCarlo(years, simulations, beginning_investment):
    total_trading = 252 * years
    results = []
    while simulations > 0:
        for i in range(0,total_trading_days):
            beginning_investment = beginning_investment * (1 + random.choice(df['SSO Return']))
            results.append(beginning_investment)
            simulations -= 1
    return results

lets_see = MonteCarlo(10,100000,10000)
plt.hist(lets_see)
plt.show()

AAR=(mean(lets_see)/20000)**(252/total_trading_days)-1

print(AAR)
print(min(lets_see))
print(max(lets_see))
