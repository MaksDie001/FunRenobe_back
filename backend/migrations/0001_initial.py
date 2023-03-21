# Generated by Django 4.1.7 on 2023-03-20 01:56

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_join', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar_img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_writer', models.BooleanField(default=False, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='Counrty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=155)),
                ('country_banner', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_join', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=155)),
                ('title', models.TextField()),
                ('group_tematic', models.TextField()),
                ('group_admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_admin', to=settings.AUTH_USER_MODEL)),
                ('group_members', models.ManyToManyField(related_name='group_members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Renobe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('date_join', models.DateField(auto_created=True, auto_now_add=True)),
                ('slug', models.SlugField()),
                ('writer_is_text', models.CharField(blank=True, max_length=155, null=True)),
                ('renobe_name', models.CharField(max_length=255)),
                ('renobe_title', models.TextField()),
                ('renobe_img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('renobe_status', models.CharField(choices=[('выпускается', 'выпускаеется'), ('работа приостановлена', 'работа приостановлена'), ('Заброшенна', 'Заброшенна')], max_length=155)),
                ('transnlation_status', models.CharField(choices=[('перевод идет', 'перевод идет'), ('перевод приостановлен', 'перевод приостановлен'), ('Заброшенна', 'Заброшенна')], max_length=155)),
                ('Note', models.CharField(default='отсутствует ', max_length=255)),
                ('country', models.ForeignKey(default='нейзвестно', on_delete=django.db.models.deletion.SET_DEFAULT, to='backend.counrty')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Renobe_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renobe_status', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=55, unique=True)),
                ('description_short', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Translation_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation_status', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Team_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Renobe_chapters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('chapter_title', models.CharField(max_length=155)),
                ('chapter_text_fiel', models.FileField(null=True, upload_to='text/%Y/%m/%d/')),
                ('audio', models.FileField(upload_to='audio/%Y/%m/%d/')),
                ('chapter_number', models.IntegerField(default=0)),
                ('renobe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Renobe', to='backend.renobe')),
                ('translators', models.ManyToManyField(related_name='transletor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['chapter_number'],
            },
        ),
        migrations.AddField(
            model_name='renobe',
            name='tags',
            field=models.ManyToManyField(to='backend.tags'),
        ),
        migrations.AddField(
            model_name='renobe',
            name='writer_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='group_tematic_tags',
            field=models.ManyToManyField(to='backend.tags'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.renobe')),
                ('self', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.comment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]