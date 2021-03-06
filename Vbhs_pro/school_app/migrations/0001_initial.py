# Generated by Django 2.0 on 2020-11-28 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('ssc', models.CharField(max_length=50)),
                ('inter', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentApply',
            fields=[
                ('studentregister',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to='school_app.StudentRegister')),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('national', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='studentlist',
            name='studentapply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.StudentApply'),
        ),
    ]
