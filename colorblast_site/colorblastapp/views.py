from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse


def index(request):
    return render_to_response("home.html", locals(), context_instance=RequestContext(request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)