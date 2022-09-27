from urllib import request
from django.shortcuts import render
from django.views.generic import View ,DetailView
from django.http import JsonResponse
from .models import *

class HomeView(View):
    def get(self,request):

        about_we = LatestResults.objects.all()
        services = Services.objects.all()
        comunity = Comunity.objects.all()
        portfolio = Portfolio.objects.all()
        p = Portfolio.objects.all()[0]
      
    
        context = {

            'about_we':about_we,
            'services':services,
            'comunity':comunity,
            'portfolio':portfolio,
            
            }

       

        return render(request,'index.html',context)



class PortfolioView(View):
    def get(self,request):
        return render(request,'portfolio.html')



class DetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio.html'
    

    

def change_lang(request):
    print('ok')
    lang = request.GET.get('current_lang')
    if lang in ['uz','ru','en']:
        request.session['lang'] = lang
    return JsonResponse({"status":200})
