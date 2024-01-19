#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saupou.settings.dev")

    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = "8080"    
    execute_from_command_line(sys.argv)
