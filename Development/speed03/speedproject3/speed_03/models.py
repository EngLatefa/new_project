from django.db import models

class Speed3(models.Model):
    Name = models.CharField(max_length=120)
    Occupation = models.TextField()
    DateofBirth = models.DateField(auto_now_add=False)
   

    def __str__(self):
        return self.Name
