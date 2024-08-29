from django.db import models
# Create your models here.


class Data(models.Model):
    roles = models.CharField(max_length=100)

    def add_role(self, role):
        if not self.roles:
            self.roles = role
        else:
            self.roles = self.roles + ", " + role

