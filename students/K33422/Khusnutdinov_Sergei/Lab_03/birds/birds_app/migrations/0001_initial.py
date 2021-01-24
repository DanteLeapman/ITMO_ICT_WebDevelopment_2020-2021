# Generated by Django 3.1.1 on 2021-01-22 23:50

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('passport', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.IntegerField(default=0)),
                ('username', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=50)),
                ('productivity', models.CharField(choices=[('low', 'Low'), ('avg', 'Average'), ('high', 'High')], max_length=4)),
                ('avg_weight', models.IntegerField(default=0)),
                ('diet', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tsekh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsekh', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(blank=True, null=True)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birds_app.cell')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField(default=0)),
                ('tsekh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birds_app.tsekh')),
            ],
        ),
        migrations.CreateModel(
            name='Chicken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('egg_amount', models.IntegerField(default=0)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birds_app.breed')),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birds_app.cell')),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birds_app.row'),
        ),
        migrations.AddField(
            model_name='cell',
            name='tsekh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birds_app.tsekh'),
        ),
        migrations.AddField(
            model_name='user',
            name='cell',
            field=models.ManyToManyField(through='birds_app.Service', to='birds_app.Cell'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]