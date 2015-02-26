import os
import sys

import django

from django.conf import settings


settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    ROOT_URLCONF="scraper.urls",
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "scraper",
    ],
    SITE_ID=1,
    TEMPLATE_DIRS=[
        os.path.abspath(os.path.join(os.path.dirname(__file__), "scraper", "tests", "templates")),
    ]
)

if hasattr(django, "setup"):
    django.setup()

from django_nose import NoseTestSuiteRunner

test_runner = NoseTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(["scraper"])

if failures:
    sys.exit(failures)
