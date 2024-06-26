# Generated by Django 4.2.3 on 2024-02-26 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letra', models.CharField(max_length=5)),
                ('texto', models.CharField(max_length=100)),
                ('correta', models.BooleanField(default=False)),
                ('pergunta_relacionada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perguntas.pergunta')),
            ],
        ),
    ]
