from django.contrib import admin

from .models import Patient,Study,Series,MR_Params,US_Params,CT_Params,Review

class StudyInline(admin.TabularInline):
    model = Study



class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['PatientName']}),
        ('Patient information', {'fields': ['PatientId', 'PatientAge', 'PatientSex', 'PatientBirthDate'],
        'classes': ['collapse']},
        ),
    ]

    inlines = [StudyInline]


class SeriesInline(admin.TabularInline):
    model = Series


class StudyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['StudyDescription']}),
        ('Study information', {'fields': ['StationName', 'ManufacturerModelName', 'StudyInstanceUID', 'Pathology',
        'StudyDate', 'StudyTime', 'AccessionNumber', 'InstitutionName', 'ReferringPhysicianName',
        'PerformingPhysicianName', 'ModalitiesInStudy'],
        'classes': ['collapse']},
        ),
    ]

    inlines = [SeriesInline]


admin.site.register(Patient, PatientAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(MR_Params)
admin.site.register(US_Params)
admin.site.register(CT_Params)
admin.site.register(Review)
