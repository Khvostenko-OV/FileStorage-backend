# Generated by Django 4.1.2 on 2023-12-09 22:38

from django.db import migrations, models
import storage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
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
                (
                    "href",
                    models.CharField(
                        default="DDbvM41OT07NyTN9PT_tqA",
                        editable=False,
                        max_length=16,
                        unique=True,
                        verbose_name="Href",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created at"
                    ),
                ),
                (
                    "expire_at",
                    models.DateTimeField(null=True, verbose_name="Expire at"),
                ),
            ],
            options={
                "verbose_name": "Link",
                "verbose_name_plural": "Links",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="StoredFile",
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
                (
                    "file",
                    models.FileField(
                        max_length=256,
                        upload_to=storage.models.owner_file_path,
                        verbose_name="File",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        default="", max_length=512, verbose_name="Description"
                    ),
                ),
                (
                    "downloads",
                    models.IntegerField(default=0, verbose_name="Download cont"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated at"
                    ),
                ),
            ],
            options={
                "verbose_name": "Stored File",
                "verbose_name_plural": "Stored Files",
                "ordering": ["pk"],
            },
        ),
    ]
