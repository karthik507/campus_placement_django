# Generated by Django 3.2.10 on 2022-01-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPO_app', '0005_companyinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200)),
            ],
        ),
    ]