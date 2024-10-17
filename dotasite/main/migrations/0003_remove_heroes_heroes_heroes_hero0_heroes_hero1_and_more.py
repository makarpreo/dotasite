# Generated by Django 5.1 on 2024-09-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_heroes_delete_mymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heroes',
            name='heroes',
        ),
        migrations.AddField(
            model_name='heroes',
            name='hero0',
            field=models.CharField(choices=[('', ''), ('orange', 'Oranges'), ('cantaloupe', 'Cantaloupes'), ('mango', 'Mangoes'), ('honeydew', 'Honeydews')], default='green', max_length=20),
        ),
        migrations.AddField(
            model_name='heroes',
            name='hero1',
            field=models.CharField(choices=[('', ''), ('orange', 'Oranges'), ('cantaloupe', 'Cantaloupes'), ('mango', 'Mangoes'), ('honeydew', 'Honeydews')], default='green', max_length=20),
        ),
        migrations.AddField(
            model_name='heroes',
            name='hero2',
            field=models.CharField(choices=[('', ''), ('orange', 'Oranges'), ('cantaloupe', 'Cantaloupes'), ('mango', 'Mangoes'), ('honeydew', 'Honeydews')], default='green', max_length=20),
        ),
        migrations.AddField(
            model_name='heroes',
            name='hero3',
            field=models.CharField(choices=[('', ''), ('orange', 'Oranges'), ('cantaloupe', 'Cantaloupes'), ('mango', 'Mangoes'), ('honeydew', 'Honeydews')], default='green', max_length=20),
        ),
    ]
