from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    #for additional attributes to the User model
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    protfolio_site = models.URLField(blank=True)
    #profile_pics inside the image field is refering the folder inside media folder
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)


    # if we need to printout a model of a UserProfileInfo. username is the default attribute
    # of the user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username