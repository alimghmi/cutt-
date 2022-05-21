from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import (
        CreateURLShortenSerializer,
        DeleteURLShortenSerializer,
)

from .models import Link, Visitor
from .utils import get_client_ip, get_shortenurl_stats


class IndexPage(TemplateView):
    
    def get(self, request):
        return HttpResponse('200')


class RedirectPage(TemplateView):
    
    def get(self, request, **kwargs):
        try:
            slug = self.kwargs.get('slug', None)
            query = Link.objects.get(slug=slug)

            if query.is_enabled:
                visitor = Visitor()
                visitor.link = query
                visitor.ip = get_client_ip(request)
                visitor.useragent = request.headers['user-agent']
                visitor.save()
                return redirect(query.origin)
            else:
                return redirect('index')
        except:
            return redirect('index')


class CreateShortenURLAPI(APIView):
    
    def post(self, request):
        try:
            serializer = CreateURLShortenSerializer(data=request.data)
            if serializer.is_valid():
                origin = serializer.data.get('origin')
            else:
                return Response({'status': 'FAIL'}, status=status.HTTP_400_BAD_REQUEST)
            
            link = Link()
            link.origin = origin
            link.save()
            data = {
                'slug': link.slug,
                'secret_slug': link.secret_slug
            }
            
            return Response({'status': 'OK', 'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'FAIL'}, status=status.HTTP_400_BAD_REQUEST)


class DeleteShortenURLAPI(APIView):

    def post(self, request):
        try:
            serializer = DeleteURLShortenSerializer(data=request.data)
            if serializer.is_valid():
                slug = serializer.data.get('slug')
            else:
                return Response({'status': 'FAIL'}, status=status.HTTP_400_BAD_REQUEST)
            
            Link.objects.get(delete_slug=slug).delete()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'FAIL'}, status=status.HTTP_400_BAD_REQUEST)


class StatsShortenURLAPI(APIView):

    def get(self, request):
        try:
            slug = request.GET['slug']
            visitors = Visitor.objects.prefetch_related('link')
            return Response({'status': 'OK', 'data': get_shortenurl_stats(visitors, slug)}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'FAIL'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateShortenURLAPI(APIView):

    def post(self, request):
        try:
            pass
        except:
            return Response({'status': 'FAIL'}, status=status.HTTP_400_BAD_REQUEST)

