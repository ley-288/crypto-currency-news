from django.shortcuts import render

def home(request):
    import requests
    import json

    #Crypto Proce
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    #Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, "home.html", {'api': api, 'price': price})

def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote'] #variable quote. what was inputed into the form is being called in quote.
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto}) #return page but passing in that quote. access on page itself by calling quote
    else:
        notfound = "Enter a crypto currency symbol into the form above..."
        return render(request, 'prices.html', {'notfound': notfound})
