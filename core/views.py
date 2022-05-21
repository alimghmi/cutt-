from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone

from datetime import datetime, timedelta

from .serializers import (
        CreateURLShortenSerializer,
        DeleteURLShortenSerializer,
)
from .models import Link, Visitor
from .utils import get_client_ip


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
            
            Link.objects.filter(slug=slug).delete()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'FAIL'}, status=status.HTTP_400_BAD_REQUEST)


class StatsShortenURLAPI(APIView):

    def get(self, request):
        try:
            slug = request.GET['slug']
            visitors = Visitor.objects.filter(link__slug = slug)
            total_visitors = visitors.count()
            last_year = visitors.filter(visited_at__gte = timezone.now() - timedelta(days=365)).count()
            last_month = visitors.filter(visited_at__gte = timezone.now() - timedelta(days=30)).count()
            last_week = visitors.filter(visited_at__gte = timezone.now() - timedelta(days=7)).count()
            yesterday = visitors.filter(visited_at__gte = timezone.now() - timedelta(days=1)).count()
            today = visitors.filter(visited_at__gte = timezone.now().date()).count()
            last_hour = visitors.filter(visited_at__gte = timezone.now() - timedelta(hours=1)).count()

            data = {
                'total': total_visitors,
                'last_year': last_year,
                'last_month': last_month,
                'last_week': last_week,
                'yesterday': yesterday,
                'today': today,
                'last_hour': last_hour,
            }

            return Response({'status': 'OK', 'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'FAIL'}, status=status.HTTP_400_BAD_REQUEST)


