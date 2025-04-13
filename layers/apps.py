'''Apps config of layer django app'''
from django.apps import AppConfig


class LayersConfig(AppConfig):
    '''Layers config setup'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'layers'
