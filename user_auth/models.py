from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from image_optimizer.fields import OptimizedImageField


import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
# Create your models here.

dept_choice = [
    ('GEN', 'General'),
    ('CSE', 'Computer Science And Engineering'),
    ('Arch', 'Architecture'),
    ('ECE', 'Electronics and Communication Engineering'),
    ('PE', 'Production Engineering'),
    ('CHE', 'Chemical Engineering'),
    ('EEE', 'Electrical and Electronics Engineering'),
    ('MEC', 'Mechanical Engineering'),
    ('CE', 'Civil Engineering')
]

course_choice = (
    ('BT', 'B.Tech'),
    ('MT', 'M.Tech'),
    ('S', 'Staff'),
    ('AL', 'Alumni'),
    ('O', 'Others')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = OptimizedImageField(default='default.png', upload_to='profile_pics')
    batch_year = models.IntegerField(default=current_year, verbose_name='Batch Year', help_text='Pass out year')
    department = models.CharField(default="GEN", choices=dept_choice, max_length=100)
    course = models.CharField(default="O", choices=course_choice, max_length=100, help_text="Ongoing")

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height >300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
