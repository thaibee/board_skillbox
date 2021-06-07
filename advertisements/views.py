import csv
from datetime import datetime, timedelta
from advertisements.models import Advertisement

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def home(request):
    ip = request.META.get('REMOTE_ADDR')
    advers = Advertisement.objects.all()
    return render(request, 'advertisements/advertisement_list.html', {'ip': ip, 'advers': advers})


def play(request):
    return render(request, 'advertisements/play.html')


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Aboutttt'
        context['name'] = 'try new function'
        return context


class Adver(View):
    def get(self, request):
        with open('log.csv', 'r') as file:
            reader = csv.reader(file)
            a = sum([1 for i in reader if
                     datetime.strptime(i[0], '%d/%m/%y %H:%M:%S') > datetime.now() - timedelta(minutes=2)])
        return render(request, 'advertisements/adver.html', {'counter': a})

    def post(self, request):
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        return render(request, 'advertisements/adver2.html', {'f_name': f_name, 'l_name': l_name})


class Contact(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['address'] = 'Lenina 18, 23'
        context['phone'] = '010-402-400'
        print(context)
        return context
