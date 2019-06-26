from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic import View
from .forms import BookInfoForm
class IndexView(View):
    def get(self,request):
        context = {
            "city":"beijing",
            "alist":[1,2,3],
            'adict':{
                'name': 'python'
            }
        }
        return render(request,"index.html",context)


class BookView(View):
    def get(self,request):
        form = BookInfoForm()
        print(1,form)
        return render(request,'book.html',{'form':form})
    def post(self,request):
        form = BookInfoForm(request.POST)
        #表单验证
        if form.is_valid():
            print(2,form.cleaned_data)
            return HttpResponse('ok')
        else:
            return render(request, 'book.html', {'form': form})
