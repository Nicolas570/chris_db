#-*- coding: utf-8 -*-

from django.db import models

################################################################################
# creation of class which match to one tables
# then we declare each field of the table
################################################################################

class Group(models.Model):
    GroupName = models.CharField(max_length=200,default='')
    GroupId = models.CharField(max_length=200,default='')
    GroupProject = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.GroupName


class User(models.Model):
    UserName = models.CharField(max_length=200,default='')
    RealName = models.CharField(max_length=200,default='')
    UserID = models.CharField(max_length=200,default='')
    Email = models.EmailField(max_length=200,default='')
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.UserName


class Patient(models.Model):
    PatientID = models.CharField(max_length=200,null=False)
    PatientName = models.CharField(max_length=200,default='')
    PatientAge = models.CharField(max_length=200,default='')
    PatientSex = models.CharField(max_length=200,default='')
    PatientBirthDate = models.CharField(max_length=200,default='')
    PatientBirthTime = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.PatientName


class Study(models.Model):
    StudyDescription = models.CharField(max_length=200,null=False)
    StationName = models.CharField(max_length=200,null=False)
    ManufacturerModelName = models.CharField(max_length=200,null=False)
    StudyInstanceUID = models.CharField(max_length=500,null=False)
    Pathology = models.CharField(max_length=200,default='')
    StudyDate = models.CharField(max_length=200,default='')
    StudyTime = models.CharField(max_length=200,default='')
    AccessionNumber = models.CharField(max_length=200,default='')
    InstitutionName = models.CharField(max_length=200,default='')
    ReferringPhysicianName =models.CharField(max_length=200,default='')
    PerformingPhysicianName = models.CharField(max_length=200,default='')
    ModalitiesInStudy = models.CharField(max_length=200,default='')
    MagneticFieldStrength = models.IntegerField(default=0)
    patient = models.ForeignKey(Patient)

    def __str__(self):
        return self.StudyDescription


class Series(models.Model):
    SeriesNumber = models.CharField(max_length=200,null=False)
    SeriesInstanceUID = models.CharField(max_length=500,null=False)
    ProtocolName = models.CharField(max_length=200,null=False)
    Modality = models.CharField(max_length=200,null=False)
    SeriesDescription = models.CharField(max_length=200,default='')
    SeriesTime = models.CharField(max_length=200,default='')
    ContrastAgent = models.CharField(max_length=200,default='')
    ScanningSequence = models.CharField(max_length=200,default='')
    BodyPartExaminated = models.CharField(max_length=200,default='')
    AcquisitionNumber =  models.CharField(max_length=200,default='')
    #MetaInfo = models.TextField(max_length=100000,default='')
    study = models.ForeignKey(Study)
    user= models.ManyToManyField(User)
    # group = models.ManyToManyField(Group)

    def __str__(self):
        return self.SeriesDescription


class MR_Params(models.Model):
    PixelSpacing = models.CharField(max_length=200,default='')
    SliceThickness = models.CharField(max_length=200,default='')
    EchoTime = models.CharField(max_length=200,default='')
    EchoNumbers = models.CharField(max_length=200,default='')
    InversionTime = models.CharField(max_length=200,default='')
    RepetitionTime = models.CharField(max_length=200,default='')
    modality_params = models.OneToOneField(Series, primary_key=True)


class US_Params(models.Model):
    Name = models.CharField(max_length=200,default='')
    modality_params = models.OneToOneField(Series, primary_key=True)

    def __str__(self):
        return self.Name


class CT_Params(models.Model):
    Name = models.CharField(max_length=200,default='')
    modality_params = models.OneToOneField(Series, primary_key=True)

    def __str__(self):
        return self.Name


# class Review(models.Model):
#     Name = models.CharField(max_length=200,default='')
#     Comment = models.CharField(max_length=200,default='')
#     Rating = models.BigIntegerField()
#     study = models.ForeignKey(Study)
#     serie = models.ForeignKey(Series)
#
#     def __str__(self):
#         return self.Name
