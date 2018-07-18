from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
@csrf_exempt
def createUser(request, method = ['POST']):
    req_data = json.loads(request.body.decode('utf-8'))
    user = User(id = req_data["id"], password = req_data["pass"])
    user.save()
    return HttpResponse(request.session['user'])

@csrf_exempt
def login(request,method = ['POST', 'GET']):
    if request.method == 'GET' :
        req_data = {
            "id" : request.GET["id"],
            "pass" : request.GET["pass"]
        }
    else :        
        print(request.body, " : BODY")
        req_data = json.loads(request.body.decode('utf-8'))
    print(req_data)
    if(User.objects.filter(id = req_data['id'])):
        user = User.objects.get(id = req_data['id'])
        if user.password == req_data['pass']:
            request.session['user'] = req_data['id']
            print(request.session['user'])
    return HttpResponse(request.session.get("user"))
# Create your views here.



@csrf_exempt
def checksession(request,method = ['POST', 'GET']):
    print(request.session['user'])
    return HttpResponse(request.session.get("user"))
#
