from django.shortcuts import render

from homepage.models  import mail, Author

def index(request):

    return render(request, 'index.html')