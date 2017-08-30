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
    
def example_chute_d_g(request):
    return render(request, os.path.join('questionnaire', 'FALL_D_SITE_DSV2_R_36_T_2017-04-21.18.36.0.html'))

def example_chute_nd_ng_h(request):
    return render(request, os.path.join('questionnaire', 'FALL_ND_SITE_QUEV_R_20_T_2017-04-25.6.15.00_heure_traitee_06.html'))
    
def example_chute_nd_ng_h1(request):
    return render(request, os.path.join('questionnaire', 'FALL_ND_SITE_QUEV_R_20_T_2017-04-25.6.15.00_heure_traitee_07.html'))

def example_chute_nd_ng_h2(request):
    return render(request, os.path.join('questionnaire', 'FALL_ND_SITE_QUEV_R_20_T_2017-04-25.6.15.00_heure_traitee_08.html'))

def example_chute_nd_ng_1h(request):
    return render(request, os.path.join('questionnaire', 'FALL_ND_SITE_QUEV_R_20_T_2017-04-25.6.15.00_heure_traitee_05.html'))

def example_chute_nd_ng_2h(request):
    return render(request, os.path.join('questionnaire', 'FALL_ND_SITE_QUEV_R_20_T_2017-04-25.6.15.00_heure_traitee_04.html'))

def example_chute_nd_g(request):
    return render(request, os.path.join('questionnaire', 'FALL_ND_SITE_QUEV_R_11_T_2017-07-13.14.00.00_heure_traitee_14.html'))
