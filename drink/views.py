from django.shortcuts import render
from drink.models import WaterInfo
import datetime
# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST.get()
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    water = WaterInfo.objects.filter(start_time__gte=now)
    print(water)
    return render(request, "index.html", {"time": now, "water": water})