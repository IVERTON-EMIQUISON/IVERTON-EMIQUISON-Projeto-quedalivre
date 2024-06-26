# Generated by Django 4.2.3 on 2024-02-26 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perguntas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_criacao', models.DateTimeField(auto_now_add=True)),
                ('correta', models.BooleanField(default=False)),
                ('alternativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perguntas.alternativa')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perguntas.pergunta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
