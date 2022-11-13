from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from .utils import get_plot
from datetime import datetime
from operator import itemgetter

cred = credentials.Certificate('openbill-be400-1bf6b9eff9e5.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Create your views here.

def index(request):
    return render(request, 'index.html')

def history(request):
    return render(request, 'history.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        enviarCorreos(name, email, subject, message)
        return redirect('/contact/') # Se hace redirect para que al recargar la página no se reenvie el mail.
    else:
        return render(request, 'contact.html')

def enviarCorreos(name, email, subject, message):
    body = {'name':name, 'email': email, 'subject': subject, 'message': message}
    template = get_template('correos.html')
    content = template.render(body)
    mail = 'openbillcorporation@gmail.com'
    sendEmail = EmailMultiAlternatives( # Estructura del correo
            'Asunto: ' + subject, # Título del correo
            'averalgo', # Cualquier cosa aquí
            settings.EMAIL_HOST_USER,
            [mail]
        )
    sendEmail.attach_alternative(content, 'text/html')
    sendEmail.send()

def login(request):
    return render(request, 'login.html')

def home(request):
    if request.method == "POST":
        # Tomar nombre del administrador
        nombreRecibido = request.POST['nombrePersona']
        contrasenaRecibida = request.POST['contrasenaPersona']
        usuarioBD = db.collection(u'usuarios')
        query = usuarioBD.where(u'user', u'==', nombreRecibido).where(u'contrasena', u'==', contrasenaRecibida)
        queryStream = query.stream()
        for usuario in queryStream:
            persona = usuario.to_dict()
        nombre = persona["nombre"]
        
        ### REALIZAR GRÁFICAS SEGÚN CADA VENDEDOR ###
        
        # Tomar nombres de los vendedores sin repetir
        facturasBD = db.collection('facturas').order_by('fecha')
        docs = facturasBD.stream()
        sellerNames = []
        for doc in docs:
            doc_dict = doc.to_dict()
            sellerNames.append(doc_dict["nombreVendedor"])
        nombresVendedores = set(sellerNames)
        
        graficasPersonales = {}
        for i in nombresVendedores:
            facturaPersona = db.collection('facturas').where('nombreVendedor', '==', i)
            docs = facturaPersona.stream()
            fechaFactura = []
            for doc in docs:
                doc_dict = doc.to_dict()
                fechaFactura.append(doc_dict)
            newList = sorted(fechaFactura, key = itemgetter('fecha','totalVenta'))
            x = [datetime.date(x["fecha"]).strftime("%Y-%m-%d") for x in newList]
            y = [y["totalVenta"] for y in newList]
            chart = get_plot(x, y)
            graficasPersonales[i] = chart
        
        if persona["tipoUsuario"] == "admin":
            return render(request, 'home.html', {"nombre": nombre, "graficasPersonales": graficasPersonales})
        else:
            messages.warning(request, "Usted no es Administrador")
            return redirect('/login/')