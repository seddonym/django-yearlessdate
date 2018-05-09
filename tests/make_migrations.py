"""This script can be used to make migrations for the testapp.
"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line
    args = sys.argv + ["makemigrations", "testapp"]
    execute_from_command_line(args)
