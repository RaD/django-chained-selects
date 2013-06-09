# -*- coding: utf-8 -*-

import locale

from django.db.models import get_model
from django.http import HttpResponse
from django.utils import simplejson


def filterchain_all(request, app_name, model_name, method_name, pk):
    Model = get_model(app_name, model_name)
    obj = Model.objects.get(pk=pk)
    qs = getattr(obj, method_name)()
    results = list(qs)
    final = []
    for item in results:
        final.append({'value': item.pk, 'display': unicode(item)})
    json = simplejson.dumps(final)
    return HttpResponse(json, mimetype='application/json')
