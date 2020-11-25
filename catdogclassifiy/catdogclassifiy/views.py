from django.http.response import HttpResponse


def helloworldfunction(request):
    returnobject = HttpResponse('hello world')
    return returnobject