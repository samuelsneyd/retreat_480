# Generated by Django 4.0.6 on 2022-07-10 23:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('alt', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2048)),
                ('image', models.ImageField(upload_to='staticfiles/images')),
                ('tags', multiselectfield.db.fields.MultiSelectField(choices=[('ACCOMMODATION', 'Accommodation'), ('OCEAN', 'Ocean'), ('BOATING', 'Boating'), ('SWIMMING', 'Swimming'), ('BIRDS', 'Birds'), ('BEACHES', 'Beaches'), ('HIKING', 'Hiking'), ('STARS', 'Stars'), ('MISC', 'Misc')], max_length=68)),
                ('priority', models.IntegerField(default=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]