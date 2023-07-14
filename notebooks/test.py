#download the top 5 cryptocurrencie by market cap from yfinance
import yfinance as yf


#write a funtion to download the top 5 cryptocurrencies by market cap
def download_data():
    #download the data
    data = yf.download(tickers = "BTC-USD ETH-USD XRP-USD USDT-USD BCH-USD", period = "1d", interval = "1d")
    #return the data
    return data
