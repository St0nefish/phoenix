from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    userid = models.OneToOneField(User)
    birthday = models.DateField()
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name 

# Create user object to attach to player object
def create_player_user_callback(sender, instance, **kwargs):
    player, new = Player.objects.get_or_create(user=instance)
post_save.connect(create_player_user_callback, User)