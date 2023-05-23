# Generated by Django 4.0 on 2023-05-23 08:38

import athena.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50, validators=[athena.models.project_name_cannont_be])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=1500)),
            ],
            options={
                'db_table': 'ProjectDB',
            },
        ),
        migrations.CreateModel(
            name='SubProjectDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('sub_project_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=1500)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.projectdb')),
            ],
            options={
                'db_table': 'SubProjectDB',
            },
        ),
        migrations.CreateModel(
            name='TrainExpDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('sub_project_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=1500)),
                ('sub_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.subprojectdb')),
            ],
            options={
                'db_table': 'TrainExpDB',
                'ordering': ['sub_project'],
            },
        ),
        migrations.CreateModel(
            name='TrainStepValLogDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('log', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('train_exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.trainexpdb')),
            ],
            options={
                'db_table': 'TrainStepValLogDB',
                'ordering': ['step'],
            },
        ),
        migrations.CreateModel(
            name='TrainStepTrainLogDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('log', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('train_exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.trainexpdb')),
            ],
            options={
                'db_table': 'TrainStepTrainLogDB',
                'ordering': ['step'],
            },
        ),
        migrations.CreateModel(
            name='TrainExpTrainInfoDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.JSONField(blank=True, default=dict)),
                ('configurations', models.JSONField(blank=True, default=dict)),
                ('options', models.JSONField(blank=True, default=dict)),
                ('description', models.CharField(blank=True, max_length=1500)),
                ('task', models.CharField(blank=True, max_length=15)),
                ('model_name', models.CharField(blank=True, max_length=30)),
                ('last_epoch', models.IntegerField(blank=True)),
                ('resume', models.BooleanField(blank=True)),
                ('train_exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.trainexpdb')),
            ],
            options={
                'db_table': 'TrainExpTrainInfoDB',
                'ordering': ['train_exp'],
            },
        ),
        migrations.CreateModel(
            name='TrainExpServerInfoDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_host_name', models.CharField(blank=True, max_length=20)),
                ('container_name', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=1500)),
                ('train_exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.trainexpdb')),
            ],
            options={
                'db_table': 'TrainExpServerInfoDB',
                'ordering': ['train_exp'],
            },
        ),
        migrations.CreateModel(
            name='TrainEpochValLogDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epoch', models.IntegerField()),
                ('log', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('train_exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.trainexpdb')),
            ],
            options={
                'db_table': 'TrainEpochValLogDB',
                'ordering': ['epoch'],
            },
        ),
        migrations.CreateModel(
            name='TrainEpochTrainLogDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epoch', models.IntegerField()),
                ('log', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('train_exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.trainexpdb')),
            ],
            options={
                'db_table': 'TrainEpochTrainLogDB',
                'ordering': ['epoch'],
            },
        ),
        migrations.CreateModel(
            name='TrainEpochSystemDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epoch', models.IntegerField()),
                ('system', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('train_exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.trainexpdb')),
            ],
            options={
                'db_table': 'TrainEpochSystemDB',
                'ordering': ['epoch'],
            },
        ),
    ]
