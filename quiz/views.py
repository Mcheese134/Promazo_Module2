from django.shortcuts import render
from django.template import loader
from django.http import Http404


from django.http import HttpResponse
from .models import Quiz, Question

def index(request):
   latest_quiz_list = Quiz.objects.order_by('id')[:5]
   context = { 'latest_quiz_list': latest_quiz_list }
   return render(request, 'quiz/index.html', context)

def detail(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'quiz/detail.html', {'question': question}) 
    return HttpResponse("You're looking at question %s." % question_id)


# Create your views here.
