# Generated by Django 3.1.3 on 2020-12-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segouser', '0002_auto_20201214_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='segouser',
            options={'verbose_name': '세고사용자', 'verbose_name_plural': '세고사용자'},
        ),
        migrations.AddField(
            model_name='segouser',
            name='email',
            field=models.CharField(default='test@gamil.com', max_length=128, verbose_name='이메일'),
            preserve_default=False,
        ),
    ]
