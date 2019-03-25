from django.shortcuts import render
from .models import Source
from .forms import SourceForm
from class_definitions import Feed_Source

# Create your views here.

def home_view(request,*args,**kwargs):
    form = SourceForm(request.POST or None)
    if form.is_valid():
        form.save()
    name=form.cleaned_data['file_name']
    l=form.cleaned_data['link']
    f= Feed_Source(name,l)
    context ={'form':form,'link1':f.articles[1].link,'description1':f.articles[1].description,'title1':f.articles[1].title}
    #print(f.articles)
    return render(request,"home.html",context)
