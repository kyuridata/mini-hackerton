from django.db import models

# Create your models here.
class Person(models.Model):
    subject = models.CharField(max_length=30)
    professor = models.CharField(max_length=30)
    def __str__(self):
            return self.subject + "(" + self.professor + ")"

class Post(models.Model):
    exam = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title