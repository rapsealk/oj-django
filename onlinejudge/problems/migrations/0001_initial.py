# Generated by Django 4.1.1 on 2022-09-12 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Problem",
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
                ("title", models.CharField(max_length=32)),
                ("description", models.TextField()),
                ("input_description", models.TextField()),
                ("input", models.TextField()),
                ("output_description", models.TextField()),
                ("output", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Submission",
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
                ("code", models.TextField()),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("C99", "C99"),
                            ("C++11", "Cxx11"),
                            ("Python 3.10.5", "Python3"),
                        ],
                        max_length=13,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("RUNNING", "Running"),
                            ("PASSED", "Passed"),
                            ("FAILED", "Failed"),
                        ],
                        default="PENDING",
                        max_length=7,
                    ),
                ),
                (
                    "problem_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="problems.problem",
                    ),
                ),
            ],
        ),
    ]
