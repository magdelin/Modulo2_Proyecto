from django.shortcuts import render, HttpResponse
from Aerolinea.models import Pasajero
# Create your views here.

def home(request):
    return render(request, "home.html")

def purchase(request):
    return render(request, "Purchase.html")

def reservation(request):
    return render(request, "Reservation.html")

#def ss(request):
    if request.method == 'GET':
        output=Person.objects.all()
        context = {
                   'VIS':'hidden',
                   'VIS1':'visibile',
                   'content': output
                   } 
        return render(request, 'Puchase.html', context)

#crear
def create(request):  
    if request.method == "POST":
        form = Pasajero(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass
    else:  
        form = ContactForm()  
    return render(request,'create.html',{'form':form})
