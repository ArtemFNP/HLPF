"""
ASGI config for PythonLB1 project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PythonLB1.settings')

application = get_asgi_application() 