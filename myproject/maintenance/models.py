from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager #EP10


class Work_request(models.Model):
	orderid = models.CharField(max_length=100)
	title = models.CharField(max_length=100,null=True,blank=True,verbose_name='รายการส่งซ่อม')
	work_order = models.CharField(max_length=100,null=True,blank=True,verbose_name='เลขwork')
	serial  = models.CharField(max_length=30,null=True,blank=True,verbose_name='serial of product')
	station = models.CharField(max_length=10,null=True,blank=True,verbose_name='station')
	bound = models.CharField(max_length=10,null=True,blank=True,verbose_name='bound')
	equipment = models.CharField(max_length=10,null=True,blank=True,verbose_name='doors') 
	detial = models.TextField(null=True,blank=True,verbose_name='รายละเอียดแจ้งซ่อม')
	sentrepairby = models.CharField(max_length=60,verbose_name='ผู้แจ้งซ่อม')
	stamp = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='วันที่แจ้ง')
	status = models.BooleanField(default=False)
	def __str__(self):
		return '{} - {} - ({}) '.format(self.title,self.detial, self.sentrepairby)
	
class Author(models.Model):
    author_name = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="auther-image/",null=True,blank=True,default="default.png")

    def __str__(self):
        return self.author_name
    
class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=280)
    description = models.TextField(max_length=280, null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    images = models.ImageField(upload_to="post-image/", null=True, blank=True)
    link = models.CharField(max_length=500,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=180, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
	
