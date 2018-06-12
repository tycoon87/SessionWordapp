from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index (request):
    return render(request,'Sessionapp/index.html')

def addword (request):
    new_word = {}
    if request.method == "POST":
        print request.POST['BOLD']
        if 'words' not in request.session:
            request.session['word'] = request.POST['word']
            request.session['color'] = request.POST['color']
            if request.POST['BOLD'] == "on":
                request.session['BOLD'] = "bold"
            else:
                request.session['BOLD'] = "normal"
    return redirect('/')

def clear (request):
    request.session.clear()
    return redirect('/')