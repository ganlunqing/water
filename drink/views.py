from django.shortcuts import render, HttpResponse
from drink.models import WaterInfo
import datetime, json
# Create your views here.

def index(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    water = WaterInfo.objects.filter(start_time__gte=now)
    print(water)
    return render(request, "index.html", {'water': water, 'time': now})

def water_start(request):
    if request.method == 'POST':
        water_start = request.POST.get("water_start")
        if water_start:
            now = datetime.datetime.now().strftime("%Y-%m-%d")
            obj = WaterInfo.objects.filter(start_time__gte=now).last()
            water = 1 if not obj else obj.water+1

            obj = WaterInfo.objects.create(water=water)
    result = {"info": "success"}
    return HttpResponse(json.dumps(result), content_type="application/json")

def water_end(request):
    if request.method == 'POST':
        water_end = request.POST.get("water_end")
        if water_start:
            now = datetime.datetime.now().strftime("%Y-%m-%d")
            obj = WaterInfo.objects.last()
            obj.end_time = datetime.datetime.now()
            obj.save()

    result = {"info": "success"}
    return HttpResponse(json.dumps(result), content_type="application/json")