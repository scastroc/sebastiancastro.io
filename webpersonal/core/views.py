from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    # print("Tipo de peticion: {}".format(request.method))
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "Mi pagina personal: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "No-contestar@inbox.mailtrap.io",
                [settings.EMAIL_HOST_USER],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")



    return render(request, "core/contact.html", {'form':contact_form})
