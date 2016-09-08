from django.shortcuts import render, get_object_or_404, HttpResponse
from questionnaire.models import Questionnaire
import os

# Create your views here.
def questionnaire_detail(request, pk):
    my_questionnaire = get_object_or_404(Questionnaire, pk=pk)
    print("Hello")
    print(my_questionnaire.filename)
    return render(request, os.path.join('questionnaire', my_questionnaire.filename) + '.html')
    
def questionnaire_list(request):
    #return HttpResponse("Congrats %s !" % "Olivier")
    questionnaires = Questionnaire.objects.all()
    return render(request, os.path.join('questionnaire', 'liste_questionnaire.html'), {'questionnaires': questionnaires})