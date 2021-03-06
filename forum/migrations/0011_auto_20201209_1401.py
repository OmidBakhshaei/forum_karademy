# Generated by Django 3.1.3 on 2020-12-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='NoSlugYet', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
