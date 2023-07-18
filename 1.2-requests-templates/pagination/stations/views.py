import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    page = int(request.GET.get('page', 1))
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        all_stations = [station for station in csv.DictReader(f)]
        paginator = Paginator(all_stations, 10)
        bus_stations = paginator.get_page(page)
        context = {
            'bus_stations': bus_stations,
            'page': bus_stations,
        }
        return render(request, 'stations/index.html', context)

