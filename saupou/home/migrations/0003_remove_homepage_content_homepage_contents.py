# Generated by Django 5.0.1 on 2024-01-18 15:30

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='content',
        ),
        migrations.AddField(
            model_name='homepage',
            name='contents',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.blocks.PageChooserBlock())], blank=True, null=True, use_json_field=True),
        ),
    ]
