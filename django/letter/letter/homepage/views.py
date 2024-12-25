from django.shortcuts import render

from homepage.models  import mail, Author

def index(request):

    return render(request, 'index.html')

def letter_view(request):
    return render(request, 'letter.html')#letter.html을 렌더링해보자

def homepage_view(request):
    return render(request, 'homepage.html')#커밋이 안되네
#커밋이 안돼!!!