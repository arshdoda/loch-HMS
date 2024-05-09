from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]

RENDERER_CLASS.append(
    "rest_framework.renderers.BrowsableAPIRenderer",
)

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

STATIC_URL = "static/"
