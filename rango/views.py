from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

# exercise 3 
def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

