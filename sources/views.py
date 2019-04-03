from django.shortcuts import render
from .models import Source
from .forms import SourceForm
from recommendations import Predefined_Sources
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
        
        if( k != True):from django.shortcuts import render
from .models import Source
from .forms import SourceForm
from recommendations import Predefined_Sources
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
        g=0
    
        #form.save()
        for i in Source.objects.all():
            if( l == i.link):
                i.name=name
                k=True
        
        if( k != True):
            form.save()

        f= Feed_Source(name,l)

        sl= Predefined_Sources()

        lst = sl.find_best_fits(f)

        for i in range(1, len(f.articles) + 1):
            context['link'+str(i)]=f.articles[i-1].link
            context['title'+str(i)]=f.articles[i-1].title
            context['description'+str(i)]=f.articles[i-1].description


        for i in range(1,len(lst[0].articles)+1):
            context[str(i)+'link']=lst[0].articles[i-1].link
            context[str(i)+'title']=lst[0].articles[i-1].title
            context[str(i)+'description']=lst[0].articles[i-1].description

        for i in range(1,len(lst[1].articles)+1):
            context[str(i)+'_link']=lst[1].articles[i-1].link
            context[str(i)+'_title']=lst[1].articles[i-1].title
            context[str(i)+'_description']=lst[1].articles[i-1].description

        sourc=Source.objects.all()
        context['Source']=sourc
        

    except Exception:   
        print("")
    #print(f.articles)'''
    
    return render(request,"home.html",context)


def item_view(request,pk):
    sourc=Source.objects.get(pk=pk)
    context={}
    try:
        f= Feed_Source(sourc.name,sourc.link)
        context['name']=sourc.name
        context['link']=sourc.link
        for i in range(1, len(f.articles) + 1):
            context['link'+str(i)]=f.articles[i-1].link
            context['title'+str(i)]=f.articles[i-1].title
            context['description'+str(i)]=f.articles[i-1].description
    except:
        print("We have a problem!!!!")
    return render(request,"saved.html",context)
    
            form.save()

        f= Feed_Source(name,l)

        sl= Predefined_Sources()

        lst = sl.find_best_fits(f)

        for i in range(1, len(f.articles) + 1):
            context['link'+str(i)]=f.articles[i-1].link
            context['title'+str(i)]=f.articles[i-1].title
            context['description'+str(i)]=f.articles[i-1].description


        for i in range(1,len(lst[0].articles)+1):
            context[str(i)+'link']=lst[0].articles[i-1].link
            context[str(i)+'title']=lst[0].articles[i-1].title
            context[str(i)+'description']=lst[0].articles[i-1].description

        for i in range(1,len(lst[1].articles)+1):
            context[str(i)+'_link']=lst[1].articles[i-1].link
            context[str(i)+'_title']=lst[1].articles[i-1].title
            context[str(i)+'_description']=lst[1].articles[i-1].description


        

    except Exception:   
        print("")
    #print(f.articles)'''
    
    return render(request,"home.html",context)
