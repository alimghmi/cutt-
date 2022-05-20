import random
import string

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