stock_list = {
  'IBM': "126.78", 
  'PNC': "156.89",
  'BUD': "98.34",
  'KO': "70.23",
  'AMZN': "105.78",
  'TSLA': "170.45",
  'AAPL': "175.78",
  'BAC': "134.67",
  'MSFT': "172.34",
  'META': "243.56"
            }

stock = input("Enter stock symbol\n:")
stock = stock.upper()
ans = stock_list.get(stock, "Ticker symbol not found")
print(ans)
