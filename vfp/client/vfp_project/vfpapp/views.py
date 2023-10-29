from django.shortcuts import render
import requests

def home(request):
    name = ""
    price = ""

    if request.GET.get("fruit"):
        fruit_name = request.GET.get("fruit")
        url = f"https://rohit1208.pythonanywhere.com/?name={fruit_name}"
        res = requests.get(url)
        data = res.json()
        
        if "msg" in data:
            msg = data["msg"]
            if "The price of" in msg and "is $" in msg:
                parts = msg.split("The price of")[1].split("is $")
                name = parts[0].strip()
                price = parts[1].strip()

    return render(request, "home.html", {"name": name, "price": price})
