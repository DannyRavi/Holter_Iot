# Generated by Django 2.2.3 on 2020-01-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bip', '0002_auto_20190708_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdata',
            name='emergency_status',
            field=models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED'), ('NOT_SEEN', 'NOT_SEEN')], default='NOT_SEEN', max_length=50),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='hospitalization',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='profiles',
            name='emergency_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='angina',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='diabetic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='family_history',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='history_of_mi',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='paec_maker',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='prior_cabg',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='prior_cath',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='smoking',
            field=models.BooleanField(default=False),
        ),
    ]
