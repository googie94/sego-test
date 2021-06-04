# Generated by Django 3.1.3 on 2021-06-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('area_group', models.CharField(blank=True, max_length=200, null=True)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'agent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Agent2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_group', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'agent2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BrainPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(blank=True, max_length=45, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('like_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'brain_post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BrainTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(blank=True, max_length=45, null=True)),
                ('tag_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'brain_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BrainUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(blank=True, max_length=45, null=True)),
                ('user_id', models.CharField(blank=True, max_length=45, null=True)),
                ('user_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'brain_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NaverComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(blank=True, max_length=45, null=True)),
                ('content', models.CharField(blank=True, max_length=500, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'naver_comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NaverPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(blank=True, max_length=45, null=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'naver_post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NaverTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(blank=True, max_length=45, null=True)),
                ('tag', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'naver_tag',
                'managed': False,
            },
        ),
    ]
