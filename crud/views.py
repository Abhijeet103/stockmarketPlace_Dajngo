from django.http import JsonResponse
from django.shortcuts import render
import requests
from  .models import Stock
# Create your views here.

token = "c07ac67fe55c1350e47d01b9599dee664a8175c2"

def getStocks(symbol , token) :
    headers = {
        'Content-Type': 'application/json'
    }
    ticker  = symbol
    metaUrl  =  f"https://api.tiingo.com/tiingo/daily/{ticker}?token={token}"
    priceUrl  = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices?token={token}"
    metaData  =  requests.get(metaUrl , headers = headers).json()
    requestResponse = requests.get(priceUrl, headers=headers)
    print(requestResponse.json())
    latest_price =  requestResponse.json()[0]['close']
    stock  = Stock(ticker  =   metaData['ticker'] ,  name  = metaData['name'] ,  description =  metaData['description'], curr_price = latest_price  )
    stock.save()

def updateStock() :
    tickers = [
        "AAPL", "MSFT", "NVDA", "TSLA", "AMZN", "GOOGL", "META", "AMD", "NFLX", "INTC",
        "ADBE", "PDD", "COST", "AVGO", "QCOM", "PYPL", "CMCSA", "CSCO", "MARA", "RIVN"
    ]
    for i in tickers :
        getStocks(i , token)

    return JsonResponse({"status": "stocks updated"})



