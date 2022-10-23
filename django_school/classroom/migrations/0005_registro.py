# Generated by Django 4.1.2 on 2022-10-12 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_quiz_fecha_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField(blank=True)),
                ('tratamiento', models.TextField(blank=True)),
                ('observaciones', models.TextField(blank=True)),
                ('fecha_registro', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('tipo_consulta', models.CharField(default='Consulta Medica', max_length=50)),
                ('examen_principal_bioquimico', models.BooleanField(default=False)),
                ('examen_principal_orina', models.BooleanField(default=False)),
                ('examen_principal_heces', models.BooleanField(default=False)),
                ('examen_principal_glucosa', models.BooleanField(default=False)),
                ('examen_resonancia_magnetica_torax', models.BooleanField(default=False)),
                ('examen_resonancia_magnetica_columna', models.BooleanField(default=False)),
                ('examen_resonancia_magnetica_cabeza', models.BooleanField(default=False)),
                ('examen_resonancia_magnetica_abdomen', models.BooleanField(default=False)),
                ('examen_ecografia_cabeza', models.BooleanField(default=False)),
                ('examen_ecografia_torax', models.BooleanField(default=False)),
                ('examen_ecografia_abdomen', models.BooleanField(default=False)),
                ('examen_ecografia_brazo', models.BooleanField(default=False)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.student')),
            ],
        ),
    ]
