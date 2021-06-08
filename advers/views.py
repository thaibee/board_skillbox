import csv
from datetime import datetime, timedelta

from advers.forms import OwnerForm, AdverForm
from advers.models import Adver, Owner

from django.shortcuts import render, HttpResponseRedirect
from django.views import View, generic
from django.views.generic import TemplateView


def home(request):
    ip = request.META.get('REMOTE_ADDR')
    advers = Adver.objects.all()
    return render(request, 'advers/advertisement_list.html', {'ip': ip, 'advers': advers})


def play(request):
    return render(request, 'advers/play.html')


class About(TemplateView):
    template_name = 'advers/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Aboutttt'
        context['name'] = 'try new function'
        return context


class Adversss(View):
    def get(self, request):
        with open('log.csv', 'r') as file:
            reader = csv.reader(file)
            a = sum([1 for i in reader if
                     datetime.strptime(i[0], '%d/%m/%y %H:%M:%S') > datetime.now() - timedelta(minutes=2)])
        return render(request, 'advers/adver.html', {'counter': a})

    def post(self, request):
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        return render(request, 'advers/adver2.html', {'f_name': f_name, 'l_name': l_name})


class Contact(TemplateView):
    template_name = 'advers/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['address'] = 'Lenina 18, 23'
        context['phone'] = '010-402-400'
        print(context)
        return context


class Advertisements(generic.ListView):
    model = Adver
    context_object_name = 'advertisements'


class AdverDetail(generic.DetailView):
    model = Adver

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        self.object.view_cnt += 1
        self.object.save()
        return data


class RegisterOwner(View):
    def get(self, request):
        owner_form = OwnerForm()
        return render(request, 'advers/register_owner.html', {'owner_form': owner_form})

    def post(self, request):
        owner_form = OwnerForm(request.POST)
        if owner_form.is_valid():
            owner_form.save()
            return HttpResponseRedirect('/')
        return render(request, 'advers/register_owner.html', {'owner_form': owner_form})


class RegisterAdver(View):
    def get(self, request):
        adver_form = AdverForm()
        return render(request, 'advers/register_adver.html', {'adver_form': adver_form})

    def post(self, request):
        adver_form = AdverForm(request.POST)
        if adver_form.is_valid():
            new_adver = Adver()
            data = adver_form.cleaned_data
            new_adver.title = data['title']
            new_adver.description = data['description']
            new_adver.price = data['price']
            print(new_adver.title, new_adver.description, new_adver.price)
            new_adver.save()
            return HttpResponseRedirect('/list/')
        return render(request, 'advers/register_adver.html', {'adver_form': adver_form})
