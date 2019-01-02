from django.shortcuts import render
from myzehut_app.models import PorteCarte, TehudaZehut, Passeport
# from myzehut_app.forms import ContactForm



# Create your views here.
def index(request):
  return render(request,'index.html')

def tehudas(request):
  tzs = TehudaZehut.objects.all()
  return render(request, 'tehuda.html', context={'tzs': tzs })

def tehuda(request , tehuda_id):
  tehuda = TehudaZehut.objects.get(id=tehuda_id)
  return render(request, 'tehud.html',context={'tehuda':tehuda})


def passeports(request):
  pss=Passeport.objects.all()
  return render (request , 'passeport.html', context={'pss':pss})

def passeport(request , passeport_id):
  ps=Passeport.objects.get(id=passeport_id)
  return render (request , 'passepor.html' , context={'ps':ps})

def portecartes(request):
  pts=PorteCarte.objects.all()
  return render ( request , 'portecarte.html' , context={'pts':pts})

def portecarte(request , portecarte_id):
  pt =PorteCarte.objects.get(id=portecarte_id)
  return render ( request , 'portecart.html' , context={'pt':pt})

def contact(request):
  if request.method == 'POST':
    subject = request.POST.get('subject')
    email = request.POST.get('email')
    text = request.POST.get('text')
    Contact.objects.get_or_create(subject=subject, email=email, text=text)
    return redirect('success/')

  return render(request, 'contact.html', context={ 'contact_form': ContactForm() })
  


