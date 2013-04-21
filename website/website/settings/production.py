# settings/production.py

from .base import *

DATABASES = {
	{
		"default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": "huiser",
		"USER": "huiser",
		"PASSWORD": get_env_variable("DATABASE_PASSWORD"),
		"HOST": "localhost",
		"PORT": "",
	}
}

SECRET_KEY = get_env_variable("SECRET_KEY")
