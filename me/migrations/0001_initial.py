# Generated by Django 4.0.3 on 2022-03-18 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieProjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CategorieProjet',
                'verbose_name_plural': 'CategorieProjets',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activite', models.CharField(max_length=50)),
                ('niveau', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Competence',
                'verbose_name_plural': 'Competences',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('date_de_naissance', models.DateField()),
                ('telephone_1', models.CharField(blank=True, max_length=10, null=True)),
                ('telephone_2', models.CharField(blank=True, max_length=10, null=True)),
                ('email_1', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_2', models.EmailField(blank=True, max_length=254, null=True)),
                ('localite', models.CharField(blank=True, max_length=50, null=True)),
                ('freelance', models.CharField(blank=True, max_length=50, null=True)),
                ('lien_cv', models.CharField(max_length=150)),
                ('lien_photo', models.CharField(max_length=150)),
                ('facebook', models.CharField(max_length=150)),
                ('twitter', models.CharField(max_length=150)),
                ('linkedin', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Me',
                'verbose_name_plural': 'Mes',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('lien', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projets', to='me.categorieprojet')),
            ],
            options={
                'verbose_name': 'Projet',
                'verbose_name_plural': 'Projets',
                'ordering': ['-created'],
            },
        ),
    ]