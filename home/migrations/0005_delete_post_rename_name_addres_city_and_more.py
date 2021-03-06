# Generated by Django 4.0.4 on 2022-06-08 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_people_specialist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.RenameField(
            model_name='addres',
            old_name='name',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='addres',
            old_name='address',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='bio',
            old_name='bio',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='case',
            new_name='medical_case',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='username',
        ),
        migrations.RemoveField(
            model_name='people',
            name='specialist',
        ),
        migrations.AddField(
            model_name='addres',
            name='street',
            field=models.CharField(default='street', max_length=10000),
        ),
        migrations.AddField(
            model_name='bio',
            name='usernames',
            field=models.OneToOneField(default='uname', on_delete=django.db.models.deletion.CASCADE, to='home.people'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients',
            field=models.ForeignKey(default='patient', on_delete=django.db.models.deletion.CASCADE, to='home.people'),
        ),
        migrations.AddField(
            model_name='people',
            name='address',
            field=models.ForeignKey(default='address', on_delete=django.db.models.deletion.CASCADE, to='home.addres'),
        ),
        migrations.AlterField(
            model_name='addres',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
