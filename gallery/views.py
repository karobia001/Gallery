from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def index(request):
    date = dt.date.today()
    images = Image.get_images()
    location = Location.get_location()
    locations = Location.get_location()

    return render(request, 'base.html', {"date": date, "images":images, "location": location, "locations": locations})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})