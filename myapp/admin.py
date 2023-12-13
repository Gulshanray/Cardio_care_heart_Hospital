from django.contrib import admin

# Register your models here.
from.models import carausel
from.models import card1
from.models import card2
from .models import *

admin.site.register(carausel)

class registration(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'docu')


admin.site.register(card1)

class registration(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'docu')

admin.site.register(card2)

class registration(admin.ModelAdmin):
    list_display = ('Dr. Name', 'sub_title', 'docu')

@admin.register(appointment)

class appAdmin(admin.ModelAdmin):
    list_display = ['yourname','youraddress','emailaddress','yourage','Date']


@admin.register(contact)
class contactForm(admin.ModelAdmin):
    list_display = ['memail', 'mphone','maddress','mcity','mstate','mpinno','mdetails']





