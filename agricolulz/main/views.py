# Create your views here.
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from agricolulz.scores.models import UserForm, User, PlayerUser


def index(request):
    context = {
        "request" : request,
    }
    print "HERE"
    return render_to_response("index.html", context)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("ok")
        else:
            return HttpResponse("no")
    else:
        return HttpResponse("invalid")

def signup(request):
    context = RequestContext(request, {
        "foo" : "bar",
    })
    if request.method == 'POST':
        f = UserForm(request.POST)
        print request.POST['username']
        print request.POST['email']
        print f.is_valid()
        #user = PlayerUser.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        if f.is_valid():
            new_user = f.save()
            print request.POST['username']
            return HttpResponse("created")
        else:
            return HttpResponse("failed")
    else:
    #return HttpResponse("ok")
        return render_to_response("signup.html", context, context_instance=RequestContext(request))

