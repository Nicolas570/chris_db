#-*- coding: utf-8 -*-

from django.db import models

class Group(models.Model):
    Name = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.Name


class User(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Password = models.CharField(max_length=200,null=False)
    Email = models.EmailField(max_length=200,null=False)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.Name


class Tag(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Color = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.Name


class Feed(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Time = models.DateTimeField(auto_now=True,null=False)
    Status = models.FloatField(null=False)
    Duration = models.BigIntegerField(null=False)
    Visible = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.Name


class Data(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Description = models.CharField(max_length=200,null=False)
    Time = models.DateTimeField(auto_now=True,null=False)
    NbFiles = models.BigIntegerField(null=False)
    Progress = models.BigIntegerField(null=False)
    user = models.ManyToManyField(User)
    feed = models.ManyToManyField(Feed)

    def __str__(self):
        return self.Name


class Token(models.Model):
    Value = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.Value
