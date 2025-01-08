from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    title = models.CharField('標題', max_length=200)
    slug = models.CharField('類別',max_length=100)
    body = models.TextField('內容')
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])
    
class Meta:
    ordering = ('-pub_date',)  # 根據發佈日期倒序排序

def __str__(self):
    return self.title
    
class CustomUser (AbstractUser ):
    nickname = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)  # 新增生日字段
    address = models.CharField(max_length=255, blank=True)  # 新增地址字段
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # 新增照片字段

    # 为 groups 和 user_permissions 添加 related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # 避免与 auth.User.groups 冲突
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # 避免与 auth.User.user_permissions 冲突
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username  # 或者其他你想要的字段

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]
