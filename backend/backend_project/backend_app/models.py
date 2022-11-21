import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
)

class ProfileTypes(models.Model):
    profile_type = models.CharField(max_length = 10, unique=True)
    
    def __str__(self) -> str:
        return self.profile_type

class UserManager(BaseUserManager):
    """
    Overriding UserManager to implement Django authentication
    within JSON Web Tokens
    """
    username = models.CharField(db_index=True, max_length=255, unique=True, error_messages={
            'unique': "A user with such username already exists, please, try another one"
        })
    def create_user(self, username, email, password):
        """
        Creates and returns a user with his username, email and password
        """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        if password is None:
            raise TypeError('Users must have a password.')    

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

class Users(AbstractUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True, error_messages={
        'unique': "A user with such username already exists, please, try another one"
    })
    email = models.EmailField(db_index=True, unique=True, error_messages={
        'unique': "This email has already been registered"
    })

    name = models.CharField(max_length = 30)
    profile_type = models.IntegerField()
    subject = models.IntegerField(default=0)

# class Users(models.Model):
#     name = models.CharField(max_length = 30)
#     email = models.CharField(max_length = 30, unique=True)
#     password = models.TextField()
#     profile_type = models.IntegerField()

#     def __str__(self) -> str:
#         return self.name

class Tasks(models.Model):
    relation_id = models.IntegerField()
    link_to_task = models.TextField()
    task_status = models.CharField(max_length = 10)
    task_comment = models.TextField()
    publication_time = models.DateTimeField()
    completion_time = models.DateTimeField()
    deadline = models.DateTimeField()

class StudentTeacher(models.Model):
    student_id = models.IntegerField()
    teacher_id = models.IntegerField()
    subject = models.IntegerField(default=0)

class Messages(models.Model):
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    message_text = models.TextField()
    sending_time = models.DateTimeField()
    is_read = models.BooleanField(default=False)

class Subjects(models.Model):
    subject = models.CharField(max_length=20, unique=True)