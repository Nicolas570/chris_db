#-*- coding: utf-8 -*-

from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.group_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=200,null=False)
    color = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.tag_name


class User(models.Model):
  user_name = models.CharField(max_length=200,null=False)
  password = models.CharField(max_length=200,null=False)
  email = models.EmailField(max_length=200,null=False)
  membership = models.ManyToManyField(Group)

  def __str__(self):
      return self.user_name


class Feed(models.Model):
  feed_name = models.CharField(max_length=200,null=False)
  time = models.DateTimeField(auto_now=True)
  progress = models.IntegerField(null=False)
  duration = models.BigIntegerField(max_length=20,null=False)
  visible = models.BooleanField(default=False)
  user = models.ForeignKey(User)
  tag = models.ManyToManyField(Tag)

  def __str__(self):
      return self.feed_name


class Patient(models.Model):
  patient_name = models.CharField(max_length=200)
  gender = models.CharField(max_length=200)
  dob = models.DateField()
  age = models.IntegerField()
  pathology = models.CharField(max_length=200,null=False)
  mrn = models.CharField(max_length=200)

  def __str__(self):
      return self.patient_name


class Study(models.Model):
  study_name = models.CharField(max_length=200,null=False)
  series_name = models.CharField(max_length=200,null=False)
  protocol_name = models.CharField(max_length=200,null=False)
  station_name = models.CharField(max_length=200,null=False)
  manufacturer_name = models.CharField(max_length=200,null=False)
  body_part_name = models.CharField(max_length=200)
  slice_thickness = models.IntegerField()
  echo_time = models.FloatField()
  magnetic_field_strenght = models.IntegerField()
  inversion_time = models.IntegerField()
  patient = models.ForeignKey(Patient)

  def __str__(self):
      return self.study_name


class Data(models.Model):
  data_name = models.CharField(max_length=200,null=False)
  description = models.CharField(max_length=200,null=False)
  time = models.DateTimeField(auto_now=True)
  nb_files = models.BigIntegerField(max_length=20,null=False)
  status = models.BigIntegerField(max_length=20,null=False)
  user = models.ManyToManyField(User)
  patient = models.ForeignKey(Patient)
  study = models.ForeignKey(Study)
  feed = models.ManyToManyField(Feed)

  def __str__(self):
      return self.data_name


class Series(models.Model):
  series_name = models.CharField(max_length=200)
  study = models.ForeignKey(Study)
  data = models.OneToOneField(Data)

  def __str__(self):
      return self.series_name


class Reviews(models.Model):
  reviews_name = models.CharField(max_length=200)
  comment = models.CharField(max_length=200)
  data = models.ForeignKey(Data)

  def __str__(self):
      return self.reviews_name


class Token(models.Model):
  value = models.CharField(max_length=200,null=False)

  def __str__(self):
      return self.value
