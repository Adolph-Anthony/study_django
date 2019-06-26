from django.shortcuts import render
# Create your views here.
from django.views.generic import View

class IndexView(View):
    def get(self,request):
        context = {
            "city":"beijing"
        }
        return render(request,"index.html",context)

