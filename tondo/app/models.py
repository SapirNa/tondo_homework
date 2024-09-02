from django.db import models
# Create your models here.


class Data(models.Model):
    userid = models.IntegerField()
    roles = models.CharField(max_length=100)

    def add_role(self, role) -> None:
        if not self.roles:
            self.roles = role
        else:
            self.roles = self.roles + ", " + role

