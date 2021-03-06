import random
import string

import requests
from rest_framework import serializers

CHARACTERS = string.ascii_letters + string.digits + '-_'


def get_random_string():
    return ''.join(random.choice(CHARACTERS) for _ in range(8))


def normalize_url(url):
    if 'http://' not in url and 'https://' not in url:
        url = 'http://' + url
    return url


def get_url(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise serializers.ValidationError(e)
    else:
        return r
