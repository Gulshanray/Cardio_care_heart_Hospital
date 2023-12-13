from django import forms
from .models import *

class appForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ['yourname', 'youraddress', 'emailaddress', 'yourage', 'Date']
        widgets = {
                'yourname':forms.TextInput(),
                'youraddress':forms.TextInput(),
                'emailaddress':forms.TextInput(),
                'yourage':forms.TextInput(),
                'Date':forms.DateInput(),

        }

class contactForm(forms.ModelForm):
    class Meta:
        Model = contact
        fields = ['memail', 'mphone','maddress','mcity','mstate','mpinno','mdetails']
        widgets = {
            'memail':forms.TextInput(),
            'mphone':forms.TextInput(),
            'maddress':forms.TextInput(),
            'mcity':forms.TextInpur(),
            'mstate':forms.TextInput(),
            'mpinno':forms.TextInpur(),
            'mdetails':forms.TextInput(),







        }

