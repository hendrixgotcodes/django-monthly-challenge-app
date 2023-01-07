from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    if(month.lower() == "january"):
        return HttpResponse("January")
    elif(month.lower() == "february"):
        return HttpResponse("february")
    elif(month.lower() == "march"):
        return HttpResponse("march")
    else:
        return HttpResponseNotFound("This month is not supported")
        