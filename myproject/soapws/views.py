from django.shortcuts import render
from suds.client import Client
from soapws.forms import CreateUserForm
from django.http import HttpResponse,HttpResponseRedirect


soap_client = Client('http://10.100.51.100:8080/lab3/UsersWS?WSDL')

def showusers(request):
    results = soap_client.service.showUsers()
    context = { 'results':results, }
    return render(request, 'soapws/allusers.html', context)


def createuser(request):
    if request.method == 'GET':
          form = CreateUserForm()
    else:
          form = CreateUserForm(request.POST)
          if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            result = soap_client.service.createUser(username,email,password)
            if result:
                return HttpResponse("User Created")
            else:
                return HttpResponse("User Not Created")

    return render(request, 'soapws/createuser.html', {
        'form': form,
    })

def getuser(request,username):
    result = soap_client.service.getUser(username)
    return render(request, 'soapws/getuser.html', {'result':result})




