# Generated by Django 5.0.2 on 2024-02-24 13:46

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_bio"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="bio",
            name="burning_desire",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bio",
            name="hobbies_and_interests",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="Testimonial",
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
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("testimonials", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("give_testimonials", "Give Testimonials"),
                            ("ask_testimonials", "Ask Testimonials"),
                        ],
                        max_length=20,
                    ),
                ),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "state_of_request",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("accepted", "Accepted"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="given_testimonials",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_testimonials",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
