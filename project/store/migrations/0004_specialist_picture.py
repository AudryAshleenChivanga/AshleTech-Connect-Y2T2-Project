# Generated by Django 5.0.6 on 2024-07-29 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_article_specialist'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='specialists/'),
        ),
    ]