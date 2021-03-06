# Generated by Django 3.2 on 2022-05-03 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predict_3class', models.TextField()),
                ('confidence_3class', models.FloatField()),
                ('predict_9class', models.TextField()),
                ('confidence_9class', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Labeling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ground_Y', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('labeling', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='visualize.labeling')),
                ('result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='visualize.result')),
            ],
        ),
        # migrations.CreateModel(
        #     name='Data',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('dataset_start', models.DateTimeField()),
        #         ('dataset_end', models.DateTimeField()),
        #         ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='AI_Model',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('status', models.TextField()),
        #         ('train_start', models.DateTimeField()),
        #         ('train_end', models.DateTimeField()),
        #         ('score', models.FloatField()),
        #         ('path', models.TextField()),
        #         ('dataset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='visualize.data')),
        #         ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
        #     ],
        # ),
    ]
