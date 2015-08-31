#-*- coding: utf-8 -*-

from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=False)
    color = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.name


class User(models.Model):
  name = models.CharField(max_length=200,null=False)
  password = models.CharField(max_length=200,null=False)
  email = models.EmailField(max_length=200,null=False)
  group = models.ManyToManyField(Group)

  def __str__(self):
      return self.name


class Feed(models.Model):
  name = models.CharField(max_length=200,null=False)
  time = models.DateTimeField(auto_now=True)
  status = models.FloatField(null=False)
  duration = models.BigIntegerField(max_length=20,null=False)
  visible = models.BooleanField(default=False)
  user = models.ForeignKey(User)
  tag = models.ManyToManyField(Tag)

  def __str__(self):
      return self.name


class Patient(models.Model):
  name = models.CharField(max_length=200)
  sex = models.CharField(max_length=200)
  birthdate = models.DateField()
  age = models.IntegerField(default=0)
  patientid = models.CharField(max_length=200)

  def __str__(self):
      return self.name


class Study(models.Model):
  name = models.CharField(max_length=200,null=False)
  pathology = models.CharField(max_length=200,null=False)
  station_name = models.CharField(max_length=200,null=False)
  manufacturer_name = models.CharField(max_length=200,null=False)
  body_part_name = models.CharField(max_length=200)
  slice_thickness = models.IntegerField(default=0)
  echo_time = models.FloatField(default=0)
  magnetic_field_strenght = models.IntegerField(default=0)
  inversion_time = models.IntegerField(default=0)
  instanceUID = models.CharField(max_length=200,null=False)
  patient = models.ForeignKey(Patient)

  def __str__(self):
      return self.name


class Data(models.Model):
  name = models.CharField(max_length=200,null=False)
  description = models.CharField(max_length=200,null=False)
  time = models.DateTimeField(auto_now=True)
  nb_files = models.BigIntegerField(max_length=20,null=False)
  progress = models.BigIntegerField(max_length=20,null=False)
  user = models.ManyToManyField(User)
  patient = models.ForeignKey(Patient)
  study = models.ForeignKey(Study)
  feed = models.ManyToManyField(Feed)

  def __str__(self):
      return self.name


class Series(models.Model):
  name = models.CharField(max_length=200)
  series_name = models.CharField(max_length=200,null=False)
  instanceUID = models.CharField(max_length=200,null=False)
  protocol_name = models.CharField(max_length=200,null=False)
  study = models.ForeignKey(Study)
  data = models.OneToOneField(Data)

  def __str__(self):
      return self.name


class Review(models.Model):
  name = models.CharField(max_length=200)
  comment = models.CharField(max_length=200)
  rating = models.BigIntegerField(max_length=20,null=False)
  data = models.ForeignKey(Data)

  def __str__(self):
      return self.name


class Token(models.Model):
  value = models.CharField(max_length=200,null=False)

  def __str__(self):
      return self.value
