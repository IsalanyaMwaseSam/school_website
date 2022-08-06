"""
WSGI config for school_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
<<<<<<< HEAD


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_website.settings')

application = get_wsgi_application()

=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_website.settings')

application = get_wsgi_application()
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_website.settings')

application = get_wsgi_application()
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
