"""
ASGI config for rosatom project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
pywebio.platform.django.wsgi_app(applications, cdn=True, static_dir=None, allowed_origins=None, check_origin=None, session_expire_seconds=None, session_cleanup_interval=None, debug=False, max_payload_size='200M', **django_options)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rosatom.settings')

application = get_asgi_application()
