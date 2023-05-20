from .base import * # noqa: F401, F403
import os 

ALLOWED_HOSTS = ["*"]
DEBUG = True 
SECRET_KEY = "DUMMY_KEY"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3") #noqa F401
    }
}