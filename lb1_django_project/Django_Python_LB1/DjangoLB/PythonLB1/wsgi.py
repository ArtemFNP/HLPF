"""
WSGI config for PythonLB1 project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PythonLB1.settings')

application = get_wsgi_application() 