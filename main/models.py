from pyexpat import model
from turtle import title
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class LatestResults(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'latest_results',null=True)
    number = models.CharField(max_length=30)


class Services(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'services',null=True)
    title = models.CharField(max_length=100)



class Comunity(models.Model):
    full_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'comunity',null=True)
    job = models.CharField(max_length=20)
    title = models.CharField(max_length=100)





class Portfolio(models.Model):
    image = models.ImageField(upload_to = 'portfolio',null=True)
    title = models.CharField(max_length=100)
    portfolio_name = models.CharField(max_length=30,null=True)

    def __str__(self) -> str:
        return self.portfolio_name



class Detail_Portfolio(models.Model):
    portfolio = models.ForeignKey(Portfolio,  on_delete=models.CASCADE,related_name='portfolio')
    detail_name = models.CharField(max_length=30,null=True)
    image = models.ImageField(upload_to = 'detail_portfolio',null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=250)
   

  




class Benefits_portfolio(models.Model):
    portfolio = models.ForeignKey(Portfolio,  on_delete=models.CASCADE,related_name='benefit')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'benefit_portfolio',null=True)
    


class Portfolio_image(models.Model):
    portfolio = models.ForeignKey(Detail_Portfolio,  on_delete=models.CASCADE,related_name='detail_portfolio')
    image = models.ImageField(upload_to = 'portfolio_image',null=True)




