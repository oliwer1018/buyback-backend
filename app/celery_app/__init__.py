import os
import sys
import django
from celery import Celery

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Ensures Django settings are loaded
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")
django.setup()

celery_app = Celery(
    "buyback",
    broker=os.getenv("REDIS_URL", "redis://redis:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://redis:6379/0")
)
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks(['celery_app'])
