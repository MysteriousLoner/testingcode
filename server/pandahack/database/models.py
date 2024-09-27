from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    total_contributions = models.IntegerField()
    bamboos = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " | contributions: " + str(self.total_contributions)


from django.db import models
from django.contrib.auth.models import User

class Pairing(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1', default="null")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2', default="null")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"{self.user1.username} - {self.user2.username}"
