from django.db import models

# Create your models here.




class blog(models.Model):
    name = models.CharField(max_length=100)
    title= models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name



# one to one field

class Username(models.Model):
    Name= models.CharField(max_length=100)
    Age= models.IntegerField()
    email = models.EmailField(max_length=1000)
    phone_number = models.IntegerField()
    adderss = models.TextField()
    image = models.ImageField(upload_to="images", blank=True,  null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Name



class test_1(models.Model):
    test = models.CharField(max_length=100) 
    user = models.OneToOneField(Username, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.email


class test_2(models.Model):
    test = models.CharField(max_length=100) 
    user = models.ForeignKey(Username, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.email
