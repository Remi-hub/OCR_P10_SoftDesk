# Generated by Django 3.2.7 on 2021-09-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=1500)),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=50)),
                ('tag', models.CharField(choices=[('Bug', 'Bug'), ('Improvement', 'Improvement'), ('Task', 'Task')], max_length=50)),
                ('status', models.CharField(choices=[('Bug', 'Bug'), ('Improvement', 'Improvement'), ('Task', 'Task')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=1500)),
                ('type', models.CharField(choices=[('Backend', 'Backend'), ('Frontend', 'Frontend'), ('iOS', 'iOS'), ('Android', 'Android')], max_length=120)),
            ],
        ),
    ]