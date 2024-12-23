from django.shortcuts import render

from homepage.models  import mail, Author

def index(request):

    #num_mails = mail.objects.all().count()

    return render(request, 'index.html')