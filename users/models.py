from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

 
    class Meta:
        verbose_name = "Courses"
        verbose_name_plural = "Courses"

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    class Meta:
        verbose_name = "Profiles"
        verbose_name_plural = "Profiles"


status_choice = (('approved', 'APPROVED'), ('pending',
                 'PENDING'), ('rejected', 'REJECTED'))


            