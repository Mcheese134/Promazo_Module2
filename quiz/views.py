from django.shortcuts import render
from django.template import loader
from django.http import Http404


from django.http import HttpResponse
from .models import Quiz

def index(request):
   latest_quiz_list = Quiz.objects.order_by('id')[:5]
   template = loader.get_template('quiz/index.html')
   context = { 'latest_quiz_list': latest_quiz_list }
   return render(request, 'quiz/index.html', context)
   # output = ', '.join([q.quiz_text for q in latest_quiz_list]) 
    #return HttpResponse("Hello This should page should contain a list of quizzes.")

#This will display the different quizzes made in the admin screen
def quiz_list(request,quiz_id): 
    return HttpResponse("This is the list of quizzes for %s" % quiz_id)

#This is the details view for a specified quiz
def detail(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist")
    return render(request, 'quiz/detail.html', {'quiz': quiz})
    #return HttpResponse("You're looking at quiz %s." % quiz_id)


# Create your views here.
