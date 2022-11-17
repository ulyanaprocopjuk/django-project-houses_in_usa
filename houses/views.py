from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import request
from django.urls import reverse
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import *
from .forms import UserLoginForm, UserRegisterForm

def index(request):
    locations = HouseLocation.objects.all()
    types = HouseType.objects.all()
    return render(request, "houses/home.html", context={
        'locations': locations,
        'types': types
    })

def catalog(request):
    houses = House.objects.all()
    types = HouseType.objects.all()
    locations = HouseLocation.objects.all()
    paginator = Paginator(houses, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'houses': houses,
        'types': types,
        'locations': locations,
        'page_obj': page_obj
    }
    return render(request, 'houses/catalog.html', context=context)

class housesSearch(ListView):
    model = House
    template_name = 'houses/houses_by_search.html'
    context_object_name = 'houses'
    paginate_by = 9

    def get_queryset(self):
        return House.objects.filter(Q(location__city__icontains=self.request.GET.get('s')) & Q(type__type_house__icontains=self.request.GET.get('c')))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"c={self.request.GET.get('s')}&{self.request.GET.get('c')}"
        context['title'] = f"{self.request.GET.get('s')} | {self.request.GET.get('c')}"
        return context

def userRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'houses/register.html', {'form': form})

def userLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'houses/login.html', {'form': form})

