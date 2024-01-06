from .base import *  # noqa: F401, F403

DATABASES = {"default": env.db_url()}  # noqa: F405
