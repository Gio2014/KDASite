# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20141206_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailtemplate',
            old_name='email',
            new_name='from_email',
        ),
    ]
