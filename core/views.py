from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView

from .models import Link

class IndexPage(TemplateView):
    
    def get(self, request):
        return HttpResponse('It worked')


class RedirectPage(TemplateView):
    
    def get(self, request, **kwargs):
        try:
            slug = self.kwargs.get('slug', None)
            query = Link.objects.get(slug=slug)

            if query.is_enabled:
                query.visits_count += 1
                query.save()
                return redirect(query.origin)
            else:
                return redirect('index')
        except:
            return redirect('index')