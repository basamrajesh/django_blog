from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

books = [
    {
        'title': "My First Book Bro",
        'author': "Basam",
        'snippet': "Abaha em rasav raa nayana book bhale undi"
    },
    {
        'title': "My Second Book",
        'author': "Basam Rajesh",
        'snippet': "Abaha em rasav raa nayana book bhale undi ani anta anukunnav kada"
    },
    {
        'title': "My Third Book",
        'author': "Basam Rajesh",
        'snippet': "Abaha em rasav raa nayana book bhale undi ani anta anukunnav kada"
    },
    {
        'title': "My Fourth Book",
        'author': "Basam Rajesh Chowdary",
        'snippet': "Abaha em rasav raa nayana book bhale undi ani anta anukunnav kada tokkale"
    },
    {
        'title': "My Fourth Book",
        'author': "Basam Rajesh Chowdary",
        'snippet': "Abaha em rasav raa nayana book bhale undi ani anta anukunnav kada tokkale"
    }
]


def home(request):
    # context = {
    #     'books': books
    # }
    return render(request, 'blog/home.html', context={'books': books})


def about(request):
    return render(request, 'blog/about.html')
