from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=260)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='image/')
    body = models.TextField()
    
    def summary(self):
        return self.body[:100]

    def pub_date_preety(self):
        return self.pub_date.strftime('%b,%e,%y')

    def __str__(self):
        return self.title