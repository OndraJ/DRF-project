# Generated by Django 4.1.6 on 2023-02-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reference", models.IntegerField()),
                ("timestamp", models.DateTimeField()),
                ("amount", models.IntegerField()),
                ("currency", models.CharField(max_length=10)),
                ("description", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
