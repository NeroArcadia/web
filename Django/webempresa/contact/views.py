from django.shortcuts import render , redirect
from django.urls import reverse
from .forms import *
from django.core.mail import EmailMessage


# Create your views here.
def contacto(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La cafeteria:Nuevo mensaje de contacto",
                "De {} <{}> \n\nEscribio: \n\n{}".format(name, email, content),
                "no-contestatar@inbox.maxltrap.io",
                ["eduardo.rosasm021@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                
                # Todo ah ido bien
                return redirect(reverse('contacto')+"?ok")
            
            except:
                #algo no ha ido bien , redireccionamos a Fail
                return redirect(reverse('contacto')+"?fail")
            
    return render(request, 'contacto.html', {'form':contact_form})

