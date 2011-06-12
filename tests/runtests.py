#!/usr/bin/env python
import os
import sys

sys.path.append('..')
backup = os.environ.get('DJANGO_SETTINGS_MODULE', '')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.test.simple import DjangoTestSuiteRunner

if __name__ == "__main__":
    runner = DjangoTestSuiteRunner(verbosity=1)
    failures = runner.run_tests(['endless_pagination'])
    if failures:
        sys.exit(failures)
    os.environ['DJANGO_SETTINGS_MODULE'] = backup
