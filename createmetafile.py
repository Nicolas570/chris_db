# -*- coding: UTF8 -*-

import datetime
import json
import sys
import random
from django.core.management.base import BaseCommand
sys.path.append('components/faker')
from faker import Faker



class Command(BaseCommand):
    help = 'writting JSON txt'

    def handle(self, *args, **options):

        fake = Faker()

        d_meta = {}
        l_history = []

        for i in range(0, 5):

            now = str(fake.date_time())

            d_meta[now] = {}

            d_meta[now]['username']     = fake.name()
            d_meta[now]['realname']     = fake.name()
            d_meta[now]['uid']          = fake.random_int(min=0, max=9999)
            d_meta[now]['email']        = fake.email()
            d_meta[now]['groupname']    = fake.name()
            d_meta[now]['gid']          = fake.random_int(min=0, max=9999)
            d_meta[now]['groupproject']      = fake.name()
            d_meta[now]['review']       = {}
            d_meta[now]['review']['comment'] = fake.text()
            d_meta[now]['review']['rating'] = fake.random_int(min=0, max=10)

            l_history.append(d_meta[now])

        with open('meta.json', 'w') as f:
            json.dump(d_meta, f)
