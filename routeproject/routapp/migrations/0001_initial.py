# Generated by Django 3.2.18 on 2023-04-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='routemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('age', models.IntegerField()),
                ('Gender', models.CharField(max_length=123)),
            ],
            options={
                'db_table': 'route_table',
            },
        ),
    ]