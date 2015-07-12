# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from main.views import *

urlpatterns = [
    # Main
    url(r'^main/buy/config/set/$', Main().main_buy_config_set),
    url(r'^main/buy/config/get/$', Main().main_buy_config_get),
    url(r'^main/buy/complete/list/get/$', Main().main_buy_complete_list_get),
    url(r'^main/buy/complete/$', Main().main_buy_complete),
    url(r'^main/buy/remove/$', Main().main_buy_remove),
    url(r'^main/buy/set/$', Main().main_buy_set),
    url(r'^main/buy/list/get/$', Main().main_buy_list_get),
    # Pages
    url(r'^$', Page().page_index),
]
