# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.db.models import Max


import json
import main.models as Models


# *****************************************************************************
# class: Page
# *****************************************************************************


class Page:

    def __init__(self):
        pass

    @staticmethod
    def page_index(request):
        """
        Событие перехода по - /
        """
        c = {}
        c.update(csrf(request))

        return render_to_response('main/index.html', c)

# *****************************************************************************
# class: Main
# *****************************************************************************


class Main:

    def __init__(self):
        pass

    @staticmethod
    def main_buy_list_get(request):
        lst_return = []
        lst_buy = Models.Buy.objects.filter(
            is_complete=False
        )
        for item in lst_buy:
            lst_return.append({
                'pk': item.pk,
                'date_create': item.date_create.strftime("%B %d, %Y"),
                'number': item.number,
                'name': item.name,
                'description': item.description
            })
        data = json.dumps(lst_return)
        return HttpResponse(data, content_type='application/json')

    @staticmethod
    def main_buy_set(request):
        str_pk = request.POST.get('pk')
        int_pk = int(request.POST.get('pk')) if str_pk else 0
        str_name = request.POST.get('title')
        str_description = request.POST.get('content')

        if int_pk:
            buy = Models.Buy.objects.get(id=int_pk)
            buy.name = str_name
            buy.description = str_description
            buy.save()
        else:
            dct_max_position = Models.Buy.objects.all().aggregate(
                Max('number')
            )
            max_number = dct_max_position['number__max']
            int_number = max_number + 1 if max_number else 1
            buy = Models.Buy.objects.create(
                number=int_number,
                name=str_name,
                description=str_description
            )
        data = json.dumps({
            'pk': buy.pk,
            'date_create': buy.date_create.strftime("%B %d, %Y"),
            'number': buy.number,
            'name': buy.name,
            'description': buy.description
        })
        return HttpResponse(data, content_type='application/json')

    @staticmethod
    def main_buy_remove(request):
        is_error = True
        str_pk = request.POST.get('pk')
        int_pk = int(request.POST.get('pk')) if str_pk else 0
        if int_pk:
            Models.Buy.objects.filter(id=int_pk).delete()
            is_error = False

        data = json.dumps({'error': is_error})
        return HttpResponse(data, content_type='application/json')

    @staticmethod
    def main_buy_complete(request):
        str_pk = request.GET.get('pk')
        int_pk = int(request.GET.get('pk')) if str_pk else 0
        buy = None
        if int_pk:
            buy = Models.Buy.objects.get(id=int_pk)
            buy.is_complete = True
            buy.save()

        data = json.dumps({
            'date_create': buy.date_create.strftime("%B %d, %Y"),
            'number': buy.number,
            'name': buy.name,
            'description': buy.description
        })
        return HttpResponse(data, content_type='application/json')

    @staticmethod
    def main_buy_complete_list_get(request):
        lst_return = []
        lst_buy = Models.Buy.objects.filter(
            is_complete=True
        ).order_by('-number')[:3]
        for item in lst_buy:
            lst_return.append({
                'date_create': item.date_create.strftime("%B %d, %Y"),
                'number': item.number,
                'name': item.name,
                'description': item.description
            })
        data = json.dumps(lst_return)
        return HttpResponse(data, content_type='application/json')

    @staticmethod
    def main_buy_config_get(request):
        data = json.dumps({
            'room': request.session.get('hipchat_room', ''),
            'token': request.session.get('hipchat_token', '')
        })
        return HttpResponse(data, content_type='application/json')

    @staticmethod
    def main_buy_config_set(request):
        str_room = request.GET.get('room')
        str_token = request.GET.get('token')
        request.session['hipchat_room'] = str_room
        request.session['hipchat_token'] = str_token
        data = json.dumps([])
        return HttpResponse(data, content_type='application/json')
