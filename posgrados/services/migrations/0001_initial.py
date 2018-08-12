# Generated by Django 2.0.6 on 2018-08-12 03:54

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
            name='Aspirante',
            fields=[
                ('id_aspirante', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_aspirante', models.CharField(max_length=20)),
                ('apellido_aspirante', models.CharField(max_length=20)),
                ('contrasena_aspirante', models.CharField(max_length=10)),
                ('dui', models.CharField(max_length=9)),
                ('genero', models.CharField(max_length=9)),
                ('fechas_nac', models.DateField()),
                ('t_fijo', models.CharField(max_length=10)),
                ('t_movil', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('titulo_pre', models.CharField(max_length=30)),
                ('institucion', models.CharField(max_length=30)),
                ('f_expedicion', models.DateField()),
                ('municipio', models.CharField(max_length=50)),
                ('lugar_trab', models.CharField(max_length=50)),
                ('programa', models.CharField(max_length=50)),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='static/f1.png', upload_to='uploads/%d-%m-%y/%H_%M_%S')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emcabezado', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now=True)),
                ('imagen', models.CharField(blank=True, max_length=250)),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Validacion',
            fields=[
                ('id_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=8)),
                ('vigencia', models.DateField()),
                ('activo', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='aspirante',
            name='id_val',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.Validacion'),
        ),
    ]
