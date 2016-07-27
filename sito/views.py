from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from product.models import *
from sito.models import *
from django.core.mail import send_mail
from filer.models import *

# Create your views here.
def HomePage(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    product_list = Product.objects.all()
    context = {'slider_list':slider_list,
                'product_list':product_list}
    return render_to_response('index.html', context, context_instance=RequestContext(request))
