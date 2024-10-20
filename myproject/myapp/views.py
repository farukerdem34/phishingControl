from django.shortcuts import render
from .models import Name


    
def index(request):
    if 'n' in request.GET and 'l' in request.GET:
        first_name = str(request.GET['n']).lower()
        last_name = str(request.GET['l']).lower()
        if Name.objects.filter(first_name=first_name,last_name=last_name).exists():
            target = Name.objects.filter(first_name=first_name,last_name=last_name).first()
            target.count=target.count+1
            target.save()
            # print("Sayaç arttı")
        else:
            Name.objects.create(first_name=first_name, last_name=last_name)
            # print("Yeni Kayıt Oluşturuldu")

    names = Name.objects.all()
    return render(request, 'index.html', {'names': names})

