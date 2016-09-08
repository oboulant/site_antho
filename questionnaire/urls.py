# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:13:53 2016

@author: OBoulant
"""

from django.conf.urls import url
from questionnaire import views

urlpatterns = [
    url(r'^$', views.questionnaire_list, name = 'questionnaire_list'),
    url(r'^questionnaire/(?P<pk>[0-9]+)/$', views.questionnaire_detail, name = 'questionnaire_detail'),
]
