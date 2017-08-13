from django.shortcuts import render,redirect
from time import gmtime, strftime

def index(request):
    return render(request, "sessionWord/index.html")

def add_word(request):
    new_word = {}
    for key,value in request.POST.items():
        new_word[key]=value

        new_word['created_at']=strftime("%Y-%m-%d %H:%M %p", gmtime())

    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    holder = request.session['words']
    holder.append(new_word)
    request.session['words'] = holder

    return redirect("/")

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
