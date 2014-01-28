from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse

from mymarketingapp.models import Client

# Create your views here.


def index(request):
    context = RequestContext(request)
    client_lists = Client.objects.all().order_by('number')

    context_dict = {
        'client_lists': client_lists
    }

    return render_to_response('mymarketingapp/index.html', context_dict, context)