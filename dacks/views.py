from functools import wraps

from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.conf.urls.defaults import url
from django.http import HttpResponse
from django.utils import simplejson

def render(template=None, **extra):
    if extra is None:
        extra = {}
    
    mimetype = extra.pop('mimetype', None)
    _format = extra.pop('format', None)
    
    def wrapper(func):
        @wraps(func)
        def decorated(request, *args, **kwargs):
            format = kwargs.pop('format', _format)
            
            data = func(request, *args, **kwargs)
            
            if isinstance(data, HttpResponse):
                return data
            
            if isinstance(data, basestring):
                return HttpResponse(data, mimetype or 'text/html')
            
            if format == 'json':
                json = simplejson.dumps(data)
                
                return HttpResponse(json, 'application/json')
            
            d = dict(extra)
            
            if data is not None:
                d.update(data)
            
            tpl = d.get('_template', template)
            
            return render_to_response(tpl, d, mimetype=mimetype,
                                context_instance=RequestContext(request))
        
        return decorated
    
    return wrapper

class Resource(list):
    def __call__(self, pattern, name=None, context=None):
        def wrapper(func):
            self.append(url(pattern, func, context, name))
            
            return func
        
        return wrapper

