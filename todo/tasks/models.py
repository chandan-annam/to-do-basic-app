from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    class select(models.IntegerChoices):
        Imporatant_Urgent = 1
        Imporatant_notUrgent = 2 
        notImporatant_Urgent = 3 
        notImporatant_notUrgent = 4

    prioritize = models.IntegerField(choices=select.choices,default=1)


    def __str__(self):
        return self.title
