# Generated by Django 4.1.3 on 2022-12-02 23:04

import autoslug.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stake', '0003_alter_chain_created_alter_chain_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chain',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, null=True, populate_from='name'),
        ),
        migrations.AlterField(
            model_name='chain',
            name='id',
            field=models.UUIDField(default=uuid.UUID('66e06f54-a188-4334-9601-4d3ebba642e1'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stake',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2246f1e8-2534-4230-a743-97d5ecd02c87'), editable=False, primary_key=True, serialize=False),
        ),
    ]
