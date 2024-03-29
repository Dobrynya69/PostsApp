# Generated by Django 4.2.1 on 2023-07-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='themes',
            field=models.ManyToManyField(blank=True, null=True, to='posts.theme'),
        ),
    ]
