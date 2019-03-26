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
    context ={'form':form,}
    for i in range(1, len(f.articles) + 1):
        context['link'+str(i)]=f.articles[i-1].link
        context['title'+str(i)]=f.articles[i-1].title
        context['description'+str(i)]=f.articles[i-1].description
    #print(f.articles)
    return render(request,"home.html",context)
