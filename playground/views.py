from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def say_hello(request: HttpRequest) -> HttpResponse:
    # You can pass in a dictionary mapping which will replace the values with jjinja2 notation
    webpage_details = {
        'name': 'Juxarius',
        'world': 'Teyvat',
        'list_of_names': [
            'Flatcat',
            'Bunbun',
            'Panda',
        ],
    }
    return render(request, 'hello.html', context=webpage_details)