from django.shortcuts import render

from django.http import HttpResponse
#from .module import Quiz

def index(request):
   # latest_quiz_list = Quiz.objects.order_by('pub_date')[:5]
   # output = ', '.join([q.quiz_text for q in latest_quiz_list]) 
    return HttpResponse("Hello This should page should contain a list of quizzes.")

#This will display the different quizzes made in the admin screen
def quiz_list(request,quiz_id): 
    return HttpResponse("This is the list of quizzes for %s" % quiz_id)

#This is the details view for a specified quiz
def detail(request, quiz_id):
    return HttpResponse("You're looking at quiz %s." % quiz_id)


# Create your views here.
