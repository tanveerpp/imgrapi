from django.db import models
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=30)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    def __str__(self) -> str:
        return self.name+' '+self.email+' '+self.address
