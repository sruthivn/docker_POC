from django.contrib.auth.models import User
from django.core.management import BaseCommand
import os

class Command(BaseCommand):
    def handle(self, *args, **options):          
        user=os.environ.get("MYSQL_ROOT_USER","root")     
        pswd=os.environ.get("MYSQL_ROOT_PASSWORD","root123")
        if not User.objects.filter(username=user).exists():              
            User.objects.create_superuser(user,'',pswd)





    

