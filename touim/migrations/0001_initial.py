# Generated by Django 3.2.4 on 2021-09-08 05:14

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
            name='Images',
            fields=[
                ('id_img', models.IntegerField(primary_key=True, serialize=False)),
                ('imgname', models.CharField(max_length=250)),
                ('imgfile', models.FileField(default='', upload_to='')),
                ('author', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Staticmap',
            fields=[
                ('id_map', models.IntegerField(primary_key=True, serialize=False)),
                ('mapname', models.CharField(max_length=250)),
                ('mapfile', models.FileField(upload_to='')),
                ('autor', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id_site', models.AutoField(primary_key=True, serialize=False)),
                ('sitename', models.CharField(max_length=500)),
                ('oper', models.CharField(max_length=250)),
                ('descr', models.CharField(default='', max_length=9000)),
                ('site_img', models.FileField(default='pasdimage.png', upload_to='')),
                ('date', models.CharField(max_length=300)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('sitename',),
            },
        ),
        migrations.CreateModel(
            name='Mobiliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mob_nom', models.CharField(max_length=250)),
                ('mob_img', models.FileField(default='pasdimage.png', upload_to='')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='touim.sites')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admini',
            fields=[
                ('id_admini', models.IntegerField(primary_key=True, serialize=False)),
                ('categ', models.CharField(max_length=250)),
                ('vid', models.CharField(max_length=100)),
                ('vid_comm', models.CharField(max_length=250)),
                ('utilisation', models.CharField(max_length=250)),
                ('herit', models.CharField(max_length=50)),
                ('infor', models.CharField(default='', max_length=9000)),
                ('descr', models.CharField(default='', max_length=9000)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='touim.sites')),
            ],
        ),
    ]
