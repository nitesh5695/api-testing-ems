# Generated by Django 3.1.6 on 2021-03-13 09:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_pa_phases_phases_question_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewed_by',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phases_question',
            name='phase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='management.pa_phases'),
        ),
    ]
