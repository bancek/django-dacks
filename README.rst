
Django Dacks
============

Django hacks for faster coding.

Installation
------------

#. Add ``dacks`` directory to your Python path.

Examples
--------

urls.py
*******

::

    from django.conf.urls.defaults import *

    urlpatterns = patterns('',
        url(r'^app/', include('app.views')),
    )

views.py
********

::

    from django.http import Http404, HttpResponseRedirect
    from django.contrib.auth.decorators import login_required
    
    from dacks.views import render, Resource
    
    # this is used instead of urls.py for our app
    resource = urlpatterns = Resource()
    
    # this decorator must always be first
    # first argument is path regex
    # second argument is name for {% url home %}
    @resource(r'^$', 'home')
    # this decorator must always be last
    # first argument is template name
    @render('home.html')
    def home(request):
        first_name = 'Jack'
        last_name = 'Sparrow'
        
        return locals()
        
        # you can now use {{ first_name }} and {{ last_name }}
        # in your home.html template
    
    # example above which is almost equal to
    @resource(r'^$', 'home')
    def home(request)
        first_name = 'Jack'
        last_name = 'Sparrow'
        
        context = {
            'first_name': first_name,
            'last_name': last_name,
        }
        
        return render_to_response('home.html', context,
                                  context_instance=RequestContext(request))
    
    @resource(r'^private$', 'private')
    # your can put other decorators between @resource and @render
    @login_required
    @render('private.html')
    def private(request):
        name = request.user.first_name
        
        return locals()
    
    @resource(r'^different-template$', 'change_template')
    @render('some_template.html')
    def change_template(request):
        this = 'fun'
        
        if 'debug' in request.GET:
            _template = 'other_template.html'
        
        return locals()
    
    @resource(r'^different/return/types$', 'different_return_types')
    @render('my_form.html')
    def diffs(request):
        if not request.user.is_authenticated():
            raise Http404
        
        form = MyForm(data=request.POST or None)
        
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('home'))
        
        return locals()
    
    @resource(r'^data.json$', 'json_example')
    @render(format='json')
    def json_example(request):
        return {
            'response': 'OK'
        }
    
    @resource(r'^data.html$', 'raw_example')
    @render()
    def raw_example(request):
        return '<html><body><h1>Hellow world</h1></body></html>'
    
    @resource(r'^data.xml$', 'mimetype_example')
    @render(mimetype='application/xml')
    def mimetype_example(request):
        return '<response><status>OK</status></response>'
