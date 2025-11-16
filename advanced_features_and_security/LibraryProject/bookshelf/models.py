from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    class Meta:
        permissions = [
            ("can_create", "Can create a book"),
            ("can_view", "Can view book"),
            ("can_delete", "Can delete book"),
            ("can_edit", "Can edit book")
        ]

   

        return f"{self.title} by {self.author} ({self.publication_year})"
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email , password, **extra_fields):
        pass
    def create_superuser(self, username, email , password, **extra_fields):
        pass



