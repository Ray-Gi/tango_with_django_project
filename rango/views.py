from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    # query Category and retrieve top 5 categories
    category_list = Category.objects.order_by('-likes')[:5]

    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage':'This tutorial has been put together by Ray Mohammed'}
    return render(request, 'rango/about.html', context = context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    # try to find a category name from the slug given
    try:
        category = Category.objects.get(slug=category_name_slug)

        # get all pages belonging to this category
        # filter returns : list of page objects 
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context=context_dict)
