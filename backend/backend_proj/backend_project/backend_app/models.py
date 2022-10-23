import datetime
from email.policy import default
from django.db import models

class Users(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 40)
    profile_type = models.CharField(max_length = 10)

    def __str__(self) -> str:
        return self.name

class Tasks(models.Model):
    relation_id = models.IntegerField()
    link_to_task = models.TextField()
    task_status = models.CharField(max_length = 10)
    task_comment = models.TextField()
    publication_time = models.DateTimeField()
    completion_time = models.DateTimeField()
    deadline = models.DateTimeField()

class Student_Teacher(models.Model):
    student_id = models.IntegerField()
    teacher_id = models.IntegerField()
    subject = models.CharField(max_length = 40)

class Messages(models.Model):
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    message_text = models.TextField()
    sending_time = models.DateTimeField()
    is_read = models.BooleanField(default=False)