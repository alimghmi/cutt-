import random
import string
from datetime import timedelta
from django.utils import timezone

ALL_CHARACTERS = string.ascii_letters

def random_slug(lenght):
    slug = ''.join(
        random.choice(ALL_CHARACTERS) for _ in range(lenght)
                )
    return slug


def generate_shorten_link(model, lenght=1):
    slug = random_slug(lenght)

    if model.__class__.objects.filter(slug=slug).exists():
        return generate_shorten_link(model, lenght+1)

    return slug


def generate_delete_link(model, lenght=16):
    slug = random_slug(lenght)

    if model.__class__.objects.filter(slug=slug).exists():
        return generate_shorten_link(model, lenght+1)

    return slug   


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def datedelta(**kwrgs):
    return timezone.now() - timedelta(**kwrgs)


def get_shortenurl_stats(visitors_instance, slug):
    try:

        visitors = visitors_instance.get(link__secret_slug = slug)
        return {
            'total': visitors.count(),
            'year': visitors.filter(visited_at__gte = datedelta(days=365)).count(),
            'month': visitors.filter(visited_at__gte = datedelta(days=30)).count(),
            'week': visitors.filter(visited_at__gte = datedelta(days=7)).count(),
            'yesterday': visitors.filter(visited_at__gte = datedelta(days=1)).count(),
            'today': visitors.filter(visited_at__gte = timezone.now().date()).count(),
            'hour': visitors.filter(visited_at__gte = datedelta(hours=1)).count(),
            'minute': visitors.filter(visited_at__gte = datedelta(minutes=1)).count(),        
        }

    except:
        raise

     
