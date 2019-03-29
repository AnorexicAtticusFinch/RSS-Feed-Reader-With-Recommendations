from django.shortcuts import render
from .models import Source
from .forms import SourceForm
from class_definitions import Feed_Source

# Create your views here.

def home_view(request,*args,**kwargs):
    form = SourceForm(request.POST or None)
    name=''
    l=''
    if form.is_valid():
        #form.save()
        {}
    context ={'form':form,}
    try:   
        name=form.cleaned_data['name']
        l=form.cleaned_data['link']
        k=False
    
        #form.save()
        for i in Source.objects.all():
            if( l == i.link):
                k=True
        
        if( k != True):
            form.save()

        f= Feed_Source(name,l)

        for i in range(1, len(f.articles) + 1):
            context['link'+str(i)]=f.articles[i-1].link
            context['title'+str(i)]=f.articles[i-1].title
            context['description'+str(i)]=f.articles[i-1].description

    except Exception:   
        print("")
    #print(f.articles)'''
    
    return render(request,"home.html",context)
