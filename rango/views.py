from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index (request):
    '''construct a dictionary to pass to the template engine as its cotext.
       note tha key boldmessae is the same as {{boldmessage}} in the template
    context_dict = {'boldmessage': "Crunchy,creamy, cookie, candy, cupcake!"}'''

    '''return a rendered response to send to the client. We make use of the
       shortcut function to make our lives easier. Note that the first
       parameter is the template we wish to use.'''


    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    
    return render(request, 'rango/index.html', context=context_dict)

def about (request):
    return render(request, 'rango/about.html')
