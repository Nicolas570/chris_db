#-*- coding: utf-8 -*-

from django.db import models


class Patient(models.Model):
    PatientId = models.CharField(max_length=200,null=False)
    PatientName = models.CharField(max_length=200,default='')
    PatientAge = models.CharField(max_length=200,default='')
    PatientSex = models.CharField(max_length=200,default='')
    PatientBirthdate = models.CharField(max_length=200,default='')
    PatientBirthTime = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.PatientName


class Study(models.Model):
    StudyName = models.CharField(max_length=200,null=False)
    Pathology = models.CharField(max_length=200,null=False)
    StationName = models.CharField(max_length=200,null=False)
    ManufacturerModelName = models.CharField(max_length=200,null=False)
    StudyInstanceUID = models.CharField(max_length=200,null=False)
    StudyDate = models.CharField(max_length=200,default='')
    StudyTime = models.CharField(max_length=200,default='')
    AccessionNumber = models.CharField(max_length=200,default='')
    InstitutionName = models.CharField(max_length=200,default='')
    ReferringPhysician =models.CharField(max_length=200,default='')
    PerformingPhysiciansName = models.CharField(max_length=200,default='')
    ModalitiesInStudy = models.CharField(max_length=200,default='')
    BodyPartExaminated = models.CharField(max_length=200,default='')
    MagneticFieldStrength = models.IntegerField(default=0)
    patient = models.ForeignKey(Patient)

    def __str__(self):
        return self.StudyName


class Series(models.Model):
    SeriesName = models.CharField(max_length=200,null=False)
    SeriesNumber = models.CharField(max_length=200,null=False)
    SeriesInstanceUID = models.CharField(max_length=200,null=False)
    ProtocolName = models.CharField(max_length=200,null=False)
    Modality = models.CharField(max_length=200,null=False)
    AccessionNumber = models.CharField(max_length=200,default='')
    SeriesDescription = models.CharField(max_length=200,default='')
    SeriesTime = models.CharField(max_length=200,default='')
    ContrastAgent = models.CharField(max_length=200,default='')
    ScanningSequence = models.CharField(max_length=200,default='')
    SeriesDescription = models.CharField(max_length=200,default='')
    BodyPartExaminated = models.CharField(max_length=200,default='')
    AcquisitionNumber = models.IntegerField(default=0)
    study = models.ForeignKey(Study)

    def __str__(self):
        return self.SeriesName


class MR_Params(models.Model):
    PixelSpacing = models.CharField(max_length=200,default='')
    SliceThickness = models.IntegerField(default=0)
    EchoTime = models.FloatField(default=0)
    EchoNumber = models.IntegerField(default=0)
    InversionTime = models.IntegerField(default=0)
    RepetionTime = models.IntegerField(default=0)
    modality_params = models.OneToOneField(Series)


class US_Params(models.Model):
    Name = models.CharField(max_length=200,default='')
    modality_params = models.OneToOneField(Series)

    def __str__(self):
        return self.Name


class CT_Params(models.Model):
    Name = models.CharField(max_length=200,default='')
    modality_params = models.OneToOneField(Series)

    def __str__(self):
        return self.Name


class Review(models.Model):
    Name = models.CharField(max_length=200,default='')
    Comment = models.CharField(max_length=200,default='')
    Rating = models.BigIntegerField()
    study = models.ForeignKey(Study)
    serie = models.ForeignKey(Series)

    def __str__(self):
        return self.Name
