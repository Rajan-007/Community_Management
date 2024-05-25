# Generated by Django 4.1.13 on 2024-05-24 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Chapter",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("last_updated_date", models.DateField(auto_now=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("online", "Online"), ("offline", "Offline")],
                        max_length=255,
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                            ("Saturday", "Saturday"),
                        ],
                        max_length=9,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChapterName",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("chapter_name", models.CharField(max_length=255)),
                ("last_updated_date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ChapterPosition",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("Chapterposition", models.CharField(max_length=255)),
                ("is_chapter", models.BooleanField(default=False)),
                (
                    "lastupdateddate",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CityData",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("city_name", models.CharField(max_length=255)),
                ("last_updated_date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="CountryData",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("country_name", models.CharField(max_length=255)),
                ("last_updated_date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="OTPVerification",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254)),
                ("otp_key", models.CharField(max_length=6)),
                (
                    "updated_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RegionPosition",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("RegionpositionName", models.CharField(max_length=255)),
                (
                    "lastupdateddate",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("isRegion", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="WeeklyPresentation",
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
                ("title", models.CharField(max_length=255)),
                ("presentation_date", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="weekly_presentations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("language", models.CharField(blank=True, max_length=100, null=True)),
                ("timezone", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_images/"
                    ),
                ),
                (
                    "company_logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="company_logos/"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TopsProfile",
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
                ("ideal_referral", models.TextField()),
                ("top_product", models.TextField()),
                ("top_problem_solved", models.TextField()),
                ("favourite_bni_story", models.TextField()),
                ("ideal_referral_partner", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tops_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
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
        migrations.CreateModel(
            name="RegionMemberPosition",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_positions",
                        to="base.regionposition",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_positions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("region_name", models.CharField(max_length=255)),
                ("last_updated_date", models.DateField(auto_now=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="regions",
                        to="base.citydata",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="regions",
                        to="base.countrydata",
                    ),
                ),
                (
                    "member_positions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="regions",
                        to="base.regionmemberposition",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("content", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("seen", models.BooleanField(default=False)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MainProfile",
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
                (
                    "title",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Mr.", "Mr."),
                            ("Mrs.", "Mrs."),
                            ("Miss", "Miss"),
                            ("Ms.", "Ms."),
                            ("Dr.", "Dr."),
                        ],
                        max_length=5,
                        null=True,
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                ("suffix", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "display_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=6
                    ),
                ),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "product_service_description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "gst_registered_state",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "gst_identification_number_or_pan",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("industry", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "classification",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "requested_speciality",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "membership_status",
                    models.CharField(
                        choices=[("Active", "Active"), ("Not Active", "Not Active")],
                        max_length=11,
                    ),
                ),
                (
                    "RenewalDueDate",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("my_business", models.TextField(blank=True, null=True)),
                ("keywords", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "Chapter",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="members",
                        to="base.chapter",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gallery",
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
                ("image", models.ImageField(upload_to="gallery_images/")),
                ("last_updated_date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GAINSProfile",
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
                ("goals", models.TextField()),
                ("accomplishments", models.TextField()),
                ("interests", models.TextField()),
                ("networks", models.TextField()),
                ("skills", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gains_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContactDetails",
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
                ("show_on_bni_public_websites", models.BooleanField(default=False)),
                ("billing_address_quick_copy", models.TextField(blank=True, null=True)),
                ("phone", models.CharField(max_length=20)),
                (
                    "direct_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("home", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "mobile_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("pager", models.CharField(blank=True, max_length=20, null=True)),
                ("voice_mail", models.CharField(blank=True, max_length=20, null=True)),
                ("toll_free", models.CharField(blank=True, max_length=20, null=True)),
                ("fax", models.CharField(blank=True, max_length=20, null=True)),
                ("email", models.EmailField(max_length=255)),
                ("receive_updates_from_bni", models.BooleanField(default=False)),
                (
                    "share_revenue_data_with_bni_director",
                    models.BooleanField(default=False),
                ),
                ("website", models.URLField(blank=True, null=True)),
                (
                    "social_networking_links",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="citydata",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cities",
                to="base.countrydata",
            ),
        ),
        migrations.CreateModel(
            name="ChapterMemberPosition",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "chapter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chapter_member_positions",
                        to="base.chapter",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chapter_member_positions",
                        to="base.chapterposition",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chapter_member_positions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="chapter",
            name="chapter_members",
            field=models.ManyToManyField(
                blank=True, related_name="chapters", to="base.mainprofile"
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chapters",
                to="base.citydata",
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chapters",
                to="base.countrydata",
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="member_positions",
            field=models.ManyToManyField(
                blank=True, related_name="chapters", to="base.chapterposition"
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chapters",
                to="base.chaptername",
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chapters",
                to="base.region",
            ),
        ),
        migrations.CreateModel(
            name="Bio",
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
                    "years_in_business",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("previous_jobs", models.TextField(blank=True)),
                ("spouse", models.CharField(blank=True, max_length=100)),
                ("children", models.CharField(blank=True, max_length=100)),
                ("pets", models.CharField(blank=True, max_length=100)),
                ("hobbies_and_interests", models.TextField(blank=True, null=True)),
                ("city_of_residence", models.CharField(blank=True, max_length=100)),
                ("years_in_city", models.PositiveIntegerField(blank=True, null=True)),
                ("burning_desire", models.TextField(blank=True, null=True)),
                ("something_no_one_knows", models.TextField(blank=True)),
                ("key_to_success", models.TextField(blank=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BillingAddress",
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
                ("should_appear", models.BooleanField(default=False)),
                ("address_line_1", models.CharField(max_length=255)),
                (
                    "address_line_2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("zip_code", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Billing",
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
                ("same_as_above", models.BooleanField(default=False)),
                (
                    "billing_address_line_1",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "billing_address_line_2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "billing_city",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "billing_state",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "billing_country",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "billing_zip_code",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("should_appear", models.BooleanField(default=False)),
                ("address_type", models.CharField(max_length=20)),
                ("address_line_1", models.CharField(max_length=255)),
                (
                    "address_line_2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("zip_code", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AccountSettings",
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
                    "bio_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "connections_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "testimonials_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "gallery_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "email_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "contact_details_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "post_notifications",
                    models.CharField(
                        choices=[
                            ("every_time", "Every time a new post is added"),
                            ("daily", "Once per day (daily digest)"),
                            ("weekly", "Once per week (weekly digest)"),
                            ("never", "Do not email me"),
                        ],
                        default="every_time",
                        max_length=10,
                    ),
                ),
                (
                    "alternate_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("forward_messages", models.BooleanField(default=False)),
                ("forward_sent_mail", models.BooleanField(default=False)),
                ("forward_connection_requests", models.BooleanField(default=False)),
                ("forward_recommendation_requests", models.BooleanField(default=False)),
                (
                    "country_settings_for_group_notifications",
                    models.CharField(default="Default", max_length=50),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_settings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Connection",
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
                    "status",
                    models.CharField(
                        choices=[("pending", "Pending"), ("accepted", "Accepted")],
                        default="pending",
                        max_length=10,
                    ),
                ),
                (
                    "connection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="connected_to",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="connections",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "connection")},
            },
        ),
    ]
