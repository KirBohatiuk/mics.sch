from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
import os


class MyUser(AbstractUser):
    username = models.CharField(verbose_name='username', max_length=100, unique=True)
    first_name = models.CharField(verbose_name='first_name', max_length=100)
    last_name = models.CharField(verbose_name='last_name', max_length=100)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    date_joined = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)


class Profile(models.Model):
    owner = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(verbose_name="bio", blank=True)
    avatar = models.ImageField('avatar', default='blank_avatar.png')

    def save(self, *args, **kwargs):
        if self.avatar:
            ext = os.path.splitext(self.avatar.name)[1]  # Get the file extension
            new_name = f'{self.owner.username}_avatar{ext}'  # Generate a new filename using the instance's primary key
            self.avatar.name = os.path.join('avatars', new_name)
        super().save(*args, **kwargs)  # Save the instance first
        if self.avatar:  # Check if image exists after saving
            img = Image.open(self.avatar.path)
            img.thumbnail((100, 75))
            img.save(self.avatar.path)


class Post(models.Model):
    owner = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    topic = models.CharField(verbose_name="topic", blank=True, max_length=50, null=True)
    text = models.CharField(verbose_name="text", blank=False, max_length=200)
    image = models.ImageField(verbose_name="post image", blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")

    def save(self, *args, **kwargs):
        if self.image:
            ext = os.path.splitext(self.image.name)[1]  # Get the file extension
            new_name = f'{self.owner.username}{ext}'  # Generate a new filename using the instance's primary key
            self.image.name = os.path.join('images', new_name)
        super().save(*args, **kwargs)  # Save the instance first
        img = Image.open(self.image.path)
        width, height = img.size
        size = min(width, height)
        left = (width - size) / 2
        top = (height - size) / 2
        right = (width + size) / 2
        bottom = (height + size) / 2
        img = img.crop((left, top, right, bottom))
        img = img.resize((458, 399), resample=Image.LANCZOS)
        img.save(self.image.path)
