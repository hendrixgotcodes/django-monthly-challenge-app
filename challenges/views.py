from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "till kitchen value struck poemze front knowledge wish",
    "february": "twicart hidden while pair putting put score way able",
    "march": "hardly death piece essential else two girl",
    "april": "ground gave buried mighty ne tight speech process height trace surprise",
    "may": "steam wore idea grass arrive et",
    "june": "wild city construction jar  break direct its",
    "july": "visit room race fellow p thou no aid",
    "august": "several steam plan allnt heard equator frequently establish",
    "september": "birthday surprise bated jet pull stick upward up fast",
    "october": "brother people love sre community equally sail forty",
    "november": "made rocket frighten refer later likely use late",
    "december": "breathing atom machidly show may dirty lunch sky",
}


# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if(month > 12 or month < 0):
        return HttpResponseNotFound("not found")

    forward_month = months[month]
    forwarded_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(forwarded_path)


def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("not found")