# Generated by Django 4.1.3 on 2022-12-13 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fichas", "0005_alter_user_telefono"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registro",
            name="tipo_consulta",
            field=models.CharField(default="Consulta médica", max_length=50, null=True),
        ),
    ]
