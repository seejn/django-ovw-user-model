from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.core.serializers.json import DjangoJSONEncoder
import json

from .models import Info
# Create your views here.

fields = [
    'id',
    'email',
    'username',
    'first_name',
    'last_name',
    'last_login',
    'date_joined',
    'address',
    'phone_number',
    'dob'
]

def decode_body(body):
    return json.loads(body)


@csrf_exempt
def index(request, **kwargs):
    
    if request.method == "GET":
        return get(request, **kwargs)
    elif request.method == "POST":
        return post(request)
    elif request.method == "PATCH":
        return patch(request, **kwargs)
    elif request.method == "DELETE":
        return delete(request, **kwargs)
    else:
        response = {
            "status": 400,
            "message": "Bad request method"
        }
        return JsonResponse(response, status=400)

def get(request, **kwargs):

    if not kwargs:
        data = Info.objects.all().values()
        data = list(data)
    else:
        user_id = kwargs.get("user_id")
        data = Info.objects.values().get(pk=user_id)

    if not data:
        status = 404
        response = {
            "message": "Data not Available",
        }
    else:
        status=200
        response = {
            "data": data
        }

    return JsonResponse(response, safe=False, status=status)

def post(request):
    if request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
    elif request.body:
        data = decode_body(request.body)
        email = data.get("email")
        password = data.get("password")

    new_user = Info.objects.create_user(email=email, password=password)

    status = 200
    msg = "New User Created."

    response = {
        "message": msg,
        "data": {
            "email": email,
            "password": password
        }
    }

    return JsonResponse(response, safe=False, status=status)

def patch(request, **kwargs):
    if not kwargs:
        response = {
            "message": "user's id required"
        }
        return JsonResponse(response, safe=False, status=404)

    user_id = kwargs.get("user_id")
    data = decode_body(request.body)
    
    user = Info.objects.get(pk=user_id)
    user.__dict__.update(data)
    user.save()

    updated_user = Info.objects.values().get(pk=user_id)
    response = {
        "message": "User Updated",
        "data": updated_user,
    }
    return JsonResponse(response, safe=False, status=200)

def delete(request, **kwargs):
    if bool(kwargs):
        user_id = kwargs.get("user_id")
        user = Info.objects.values().get(pk=user_id)
        Info.objects.get(pk=user_id).delete()
        
        status = 200
        message = "User deleted successfully"

        response = {
            "message": message,
            "data": user,
        }
        return JsonResponse(response, safe=False, status=status)

    status = 200
    msg = "user's id required to hit this request"

    response = {
        "message": msg
    }
    
    return JsonResponse(response, safe=False, status=status)