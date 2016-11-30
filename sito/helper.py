# coding=utf-8
from datetime import *


from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from product.models import *
from product.forms import *
from sito.models import *
from cart.models import *
from order.models import *
from django.core.mail import send_mail
from filer.models import *
#
#login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect

from django.db.models import Sum
from decimal import *
from decimal import Decimal

from django.contrib import messages




# da che data a che data si visualizzerà l'inverno Da FEBBRAIO A FINE AGOSTO
# da che data a che data si visualizzerà l'estate DA SETTEMBRE A FINE GENNAIO
def get_stagione(inizio, fine):
    oggi = datetime.now().date()
    if inizio < oggi < fine:
        return "INVERNO"
    else:
        return "ESTATE"
    
    


# controlla magazzino e scarica
def check_magazzino(qt_richiesta, qt_magazzino, compi):
    if qt_magazzino > 0 or qt_magazzino >= qt_richiesta:
        print "quantita richiesta ok"
        quantita = qt_magazzino - qt_richiesta
        if quantita >=0:
            compi.quantity = quantita
            compi.save()
            return True
        else:
            return False
    else:
        #order.delete()
        return False



def check_ifPresent(comp, lista):
    if comp in lista:
        return True
    else:
        return False


