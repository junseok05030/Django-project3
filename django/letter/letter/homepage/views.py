from django.shortcuts import render

from homepage.models  import Mail, Author

def index(request):

    return render(request, 'index.html')