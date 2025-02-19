# Generated by Django 5.1.5 on 2025-02-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0004_alter_record_paid_alter_record_specialization"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recognition",
            fields=[
                ("recognition_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("type_of_recognition", models.CharField(max_length=255)),
                ("institution", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("image_id", models.CharField(blank=True, max_length=255, null=True)),
                ("thumbnail", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
