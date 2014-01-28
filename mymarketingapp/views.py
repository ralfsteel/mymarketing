from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect

from mymarketingapp.models import Client, Pricelist, Promotional
from mymarketingapp.forms import ClientForm

# Create your views here.


def customer(request):
    client_lists = Client.objects.all().order_by('number')
    context = RequestContext(request)
    if request.method == 'Post':
        form = ClientForm(request.post)
        if form.is_valid():
            return HttpResponseRedirect('/Thanks/')
        else:
            form = ClientForm()

    context_dict = {
        'client_lists': client_lists,
        'form': form
    }

    return render_to_response('mymarketingapp/customer.html', context_dict, context)

def pricing(request):
    context = RequestContext(request)
    price_lists = Pricelist.objects.all()

    context_dict = {
        'price_lists': price_lists
    }

    return render_to_response('mymarketingapp/pricing.html', context_dict, context)

def detail(request):
    context = RequestContext(request)
    item_details = Promotional.objects.all()

    context_dict = {
        'item_details': item_details
    }

    return render_to_response('mymarketingapp/detail.html', context_dict, context)