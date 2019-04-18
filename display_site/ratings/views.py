from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.



def index(request):
    business = models.Business.objects.all()
    businesses = {"businesses": business}
    return render(request, 'ratings/index.html', context=businesses)
    # return HttpResponse(business)
