
from django import forms

from mymarketingapp import Client

class ClientFrom(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Please enter your full  name")
    address = forms.CharField(max_lenght=128, help_text="Please enter you address")
    zipcode = forms.IntegerField(default=0)
    city = forms.CharField(max_length=128, help_text="Please enter the city name")
    phone = forms.IntegerField(default=0)
    phones = forms.IntegerField(default=0)
    fax = forms.IntegerField(default=0)
    email = forms.EmailField()

    class Meta:
        model = Client
        fields = ['name','address','zipcode','city','phone','phones','fax','email']
