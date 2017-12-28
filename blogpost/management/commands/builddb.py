"""
bangazon custom command to build database
"""

from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations
# from blogpost.factories import *

class Command(BaseCommand):
    """
    Defines the command 'builddb', which is a shortcut for running
    the necessary shell commands to generate our database's tables and
    load our data to them via Faker. These commands are, in order:
    1. python manage.py makemigrations api
    2. python manage.py migrate
    3. (Factory Calls): Category, User, Payment, Product, ProductOrder


    Author: stolen from bangazon
    """

  
    def handle(self, *args, **options):
        management.call_command('makemigrations')
        management.call_command('migrate')



    
