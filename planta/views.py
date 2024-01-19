from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.



def abhitnal(request):
    return render (request, 'abhitnal.html')


def myview(request):
    return render (request, 'bitnal.html')




def mydecor(view_func):
    def wrapper(request, *args, **kwargs):
        print("Something is happening before the view is called.")
        response = view_func(request, *args, **kwargs)
        print("Something is happening after the view is called.")
        return response
    return wrapper

@mydecor 
def mynano(request):
    return JsonResponse({'message':'hellow world '}) 

