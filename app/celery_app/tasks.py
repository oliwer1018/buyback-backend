from . import celery_app

@celery_app.task
def test_add(x, y):
    return x + y
