"""
ASGI config for ONT_MAC_Data_Report_Dashboard project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ONT_MAC_Data_Report_Dashboard.settings')

application = get_asgi_application()
