# Generated by Django 4.0.4 on 2022-06-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_trabalhocurso_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalhocurso',
            name='descricao',
            field=models.TextField(),
        ),
    ]
