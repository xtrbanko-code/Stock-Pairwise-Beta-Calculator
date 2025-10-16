import yfinance as yf
import numpy as np
import datetime as dt

stock = str(input('What is your first ticker? ')).upper()
stock_ref = str(input('What is your second ticker? ')).upper()
years = float(input('How many years would you like to look at? '))
data = (yf.download([stock, stock_ref], start = (dt.datetime.now() - dt.timedelta(days = 365*3)), end = dt.datetime.now(), auto_adjust = True)['Close'])
data = data.dropna()
returns = (np.log(data / data.shift(1))).iloc[1:]
cov = np.cov(returns[stock].to_numpy(), returns[stock_ref].to_numpy())[0,1]
var = np.var(returns[stock_ref].to_numpy())
beta = cov / var
print('Pairwise Beta: ' + str(round(beta, 4)))
input('Click Enter to Exit')
exit()