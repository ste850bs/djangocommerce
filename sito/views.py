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
from django.core.mail import send_mail
from filer.models import *
#
#login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect







# Create your views here.


@login_required(login_url="login/")
def HomePage(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    last_list = Product.objects.all().order_by('-pub_date')[:4]
    promo_list = Product.objects.filter(promo=True).filter(slide = True).order_by('-pub_date')[:4]
    offerte_list = Product.objects.filter(promo=True).order_by('-id')[:4]
    product_list = Product.objects.all()[:4]
    context = {'slider_list':slider_list,
    			'last_list':last_list,
    			'promo_list':promo_list,
                'product_list':product_list,
                'offerte_list':offerte_list}
    return render_to_response('index.html', context, context_instance=RequestContext(request))



@login_required(login_url="login/")
def ProductFilterCategory(request, post_id):
    product_list = Product.objects.filter(category__in=post_id)
    context = {'product_list': product_list}
    return render_to_response('price_list.html', context, context_instance=RequestContext(request))


@login_required(login_url="login/")
def ProductFilterTag(request, post_id):
    product_list = Product.objects.filter(tags__in=post_id)
    context = {'product_list': product_list}
    return render_to_response('category_list.html', context, context_instance=RequestContext(request))


@login_required(login_url="login/")
def product_list(request):
    product_list = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'price_list.html', {'product_list': product_list})


@login_required(login_url="login/")
def ProductFilterView(request, post_id):
    product = Product.objects.get(pk=post_id)
    filer_list = Image.objects.filter(folder_id = product.album)
    lunghezzacinture_list = CintureLunghezza.objects.all()
    tagliascarpe_list = TagliaScarpe.objects.all()
    form = ProductForm()
    context = {'product': product,
    			'filer_list':filer_list,
                'lunghezzacinture_list':lunghezzacinture_list,
                'tagliascarpe_list':tagliascarpe_list,
                'form':form}
    return render_to_response('detail.html', context, context_instance=RequestContext(request))


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')






## cart
'''
@login_required(login_url="login/")
def add_to_cart(request):
    request.session['cart_list']=[]
    cart_list = request.session['cart_list']
    product = request.POST.get("product_id")
    color = request.POST.get("color_id")
    cart_list = cart_list+[[product,color]]
    request.session['cart_list'] = cart_list
    context = {'cart_list':cart_list}
    return render_to_response("cart.html", context, context_instance=RequestContext(request))'''



def add_to_cart(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = AddForm()
    return render(request, 'cart-form.html', {'form': form})


###  GLOBALI ###
def CategoryMenuView(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return context
