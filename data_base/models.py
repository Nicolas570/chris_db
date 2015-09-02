#-*- coding: utf-8 -*-

from django.db import models


class Patient(models.Model):
    PatientName = models.CharField(max_length=200)
    PatientSex = models.CharField(max_length=200)
    PatientBirthdate = models.DateField()
    PatientAge = models.IntegerField(default=0)
    PatientId = models.CharField(max_length=200)

    def __str__(self):
        return self.PatientName


class Study(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Pathology = models.CharField(max_length=200,null=False)
    StationName = models.CharField(max_length=200,null=False)
    ManufacturerModelName = models.CharField(max_length=200,null=False)
    BodyPartExaminated = models.CharField(max_length=200)
    MagneticFieldStrength = models.IntegerField(default=0)
    Modality = models.CharField(max_length=200,null=False)
    StudyInstanceUID = models.CharField(max_length=200,null=False)
    patient = models.ForeignKey(Patient)

    def __str__(self):
        return self.Name


class Series(models.Model):
    Name = models.CharField(max_length=200,null=False)
    SeriesName = models.CharField(max_length=200,null=False)
    SeriesInstanceUID = models.CharField(max_length=200,null=False)
    ProtocolName = models.CharField(max_length=200,null=False)
    study = models.ForeignKey(Study)

    def __str__(self):
        return self.Name


class MR_Params(models.Model):
    Name = models.CharField(max_length=200)
    SliceThickness = models.IntegerField(default=0)
    EchoTime = models.FloatField(default=0)
    InversionTime = models.IntegerField(default=0)
    RepetionTime = models.IntegerField(default=0)
    modality_params = models.OneToOneField(Series)

    def __str__(self):
        return self.Name


class US_Params(models.Model):
    Name = models.CharField(max_length=200)
    modality_params = models.OneToOneField(Series)

    def __str__(self):
        return self.Name


class CT_Params(models.Model):
    Name = models.CharField(max_length=200)
    modality_params = models.OneToOneField(Series)

    def __str__(self):
        return self.Name


class Review(models.Model):
    Name = models.CharField(max_length=200)
    Comment = models.CharField(max_length=200)
    Rating = models.BigIntegerField()
    study = models.ForeignKey(Study)
    serie = models.ForeignKey(Series)

    def __str__(self):
        return self.Name
