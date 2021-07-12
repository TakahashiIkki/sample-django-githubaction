# -*- coding:utf-8 -*-
# ローカル設定

from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sampledb',
        'USER': 'ikki',
        'PASSWORD': 'sampledb123',
        'HOST': 'postgres-db',
    }
}

# page_sizeのデフォルト値を定義
REST_FRAMEWORK['PAGE_SIZE'] = 10
