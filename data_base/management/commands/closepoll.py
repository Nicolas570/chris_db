import os
from django.core.management.base import BaseCommand
from data_base.models import User, Group





class Command(BaseCommand):
    help = 'it read user.txt'


    def handle(self, *args, **options):

       for dossier, sous_dossiers, fichiers in os.walk('/neuro/users/nicolas.charlet/ChrisDbTest'):
           for fichier in fichiers:
               fullpath = os.path.join(dossier, fichier)
               if fichier.endswith('user.txt'):
                print(fullpath)
                ds = read_file(fullpath)
