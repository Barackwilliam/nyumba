# Generated by Django 5.1.1 on 2025-03-20 20:16

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jina', models.CharField(max_length=50)),
                ('Cheo', models.CharField(max_length=50)),
                ('image_of_agent', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('facebook_link', models.URLField(blank=True, max_length=300, null=True)),
                ('twitter_link', models.URLField(blank=True, max_length=300, null=True)),
                ('instagram_link', models.URLField(blank=True, max_length=300, null=True)),
                ('linkedIn', models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('client_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('location', models.CharField(max_length=50)),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('offer_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jina', models.CharField(max_length=50)),
                ('image_of_partners', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='PopularPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_place', models.CharField(max_length=50)),
                ('number_of_property', models.IntegerField()),
                ('image_of_place', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Myapp_payment',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('owner', 'Owner'), ('customer', 'Customer')], default='customer', max_length=20)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('bio', models.TextField(blank=True, max_length=250)),
                ('profile_picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('verified_at', models.DateTimeField(blank=True, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('subscription_plan', models.CharField(choices=[('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum')], default='silver', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('For Rent', 'For Rent'), ('For Sale', 'For Sale')], max_length=30)),
                ('p_status', models.CharField(choices=[('Active', 'Active'), ('Sold', 'Sold')], max_length=30)),
                ('property_type', models.CharField(choices=[('Apartment', 'Apartment'), ('House', 'House'), ('Commercial', 'Commercial')], max_length=10)),
                ('country', models.CharField(default='Tanzania', max_length=25)),
                ('region', models.CharField(choices=[('ARS', 'Arusha'), ('DSM', 'Dar es salaam'), ('DDM', 'Dodoma'), ('RVM', 'Ruvuma'), ('TBR', 'Tabora'), ('MBY', 'Mbeya'), ('MRG', 'Morogoro'), ('LND', 'Lindi'), ('KGM', 'Kigoma'), ('KTV', 'Katavi'), ('GIT', 'Geita'), ('MNR', 'Manyara'), ('KLR', 'Kilimanjaro'), ('MR', 'Mara'), ('MTR', 'Mtwara'), ('MZ', 'Mwanza'), ('NB', 'Njombe'), ('SNG', 'Songwe'), ('TNG', 'Tanga'), ('SNG', 'Shinyanga'), ('IRN', 'Iringa'), ('KGR', 'Kagera'), ('PMB', 'Pemba Kaskazini'), ('PK', 'Pemba Kusini'), ('PN', 'Pwani'), ('RK', 'Rukwa'), ('SGD', 'Singida'), ('SMY', 'Simiyu'), ('ZKA', 'Zanzibar Kaskazini'), ('ZKU', 'Zanzibar Kusini'), ('ZMG', 'Zanzibar Mjini Magharibi')], max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('ward', models.CharField(max_length=30)),
                ('is_available', models.BooleanField(default=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('view_count', models.IntegerField(default=0)),
                ('business_phone', models.CharField(max_length=13)),
                ('business_email', models.EmailField(max_length=60)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('house_size', models.IntegerField()),
                ('nearby', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image1', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image2', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image3', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('property_owner', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('video_link', models.URLField(blank=True, max_length=300, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('viewers', models.ManyToManyField(blank=True, related_name='viewed_properties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PopularProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('p_property_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='popular_properties', to='Myapp.property')),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.property')),
            ],
        ),
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('f_property_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='featured_properties', to='Myapp.property')),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.property')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_code', models.CharField(max_length=10, unique=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rewarded', models.BooleanField(default=False)),
                ('referred_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referred_by', to=settings.AUTH_USER_MODEL)),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
