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
    url(r'^example_chute_d_g/', views.example_chute_d_g, name = 'example_chute_d_g'),
    url(r'^example_chute_nd_ng_h/', views.example_chute_nd_ng_h, name = 'example_chute_nd_ng_h'),
    rl(r'^example_chute_nd_ng_h1/', views.example_chute_nd_ng_h1, name = 'example_chute_nd_ng_h1'),
    rl(r'^example_chute_nd_ng_h2/', views.example_chute_nd_ng_h2, name = 'example_chute_nd_ng_h2'),
    rl(r'^example_chute_nd_ng_2h/', views.example_chute_nd_ng_2h, name = 'example_chute_nd_ng_2h'),
    rl(r'^example_chute_nd_g/', views.example_chute_nd_g, name = 'example_chute_nd_g'),
]
