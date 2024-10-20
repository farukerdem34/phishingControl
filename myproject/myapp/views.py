from django.shortcuts import render
from .models import Name


    
def index(request):
    if 'first_name' in request.GET and 'last_name' in request.GET:
        first_name = request.GET['first_name']
        last_name = request.GET['last_name']
        
        Name.objects.create(first_name=first_name, last_name=last_name)

    names = Name.objects.all()
    return render(request, 'index.html', {'names': names})
