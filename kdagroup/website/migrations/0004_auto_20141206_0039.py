# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_emailform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailForm',
            new_name='EmailTemplate',
        ),
    ]
