from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
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



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .models import UserInfo  # Make sure this import is correct


@login_required
def index(request) :
    return render(request , 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')


        panCard = request.POST.get('panCard')
        phoneNumber = request.POST.get('phoneNumber')
        profile_pic = request.FILES.get('profile_pic')
        panCard_Image = request.FILES.get('panCard_Image')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register.html')


        user = User(username=username, email=email)
        user.set_password(password)
        user.save()


        user_info = UserInfo(
            user=user,
            panCard=panCard,
            phoneNumber=phoneNumber,
            profile_pic=profile_pic,
            panCard_Image=panCard_Image
        )
        user_info.save()

        login(request, user)
        return redirect('index')

    return render(request, 'register.html')


# make login logout

def loginView(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  authenticate(username ,  password)
        if user  :
            login(request ,  user)
            return  redirect('index')

        return  render(request ,  'login.html')


def logout_view(request) :
    logout(request)

