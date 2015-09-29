import os, pydicom, json
from django.core.management.base import BaseCommand
from polls.models import Patient, Study, Series, MR_Params, US_Params, CT_Params, User, Group

class Command(BaseCommand):
    help = 'Finding .dcm files and complite tables'


    def handle(self, *args, **options):

################################################################################
# frist this application read the dcm list file which contain each path of each
# frist dicom of each dicom folders.
# then we use all those paths and we change the path to get the meta.json file
################################################################################


        #dcmTree = '/neuro/users/nicolas.charlet/CodeDcmDb/db_dcm.lst'
        dcmTree = '/neuro/users/nicolas.charlet/db_dcm.lst'

        if len(args) == 2:
            if args[0] == 'path':
                dcmTree = args[1]


        data = [line.strip() for line in open(dcmTree, 'r')]
        N_lignes = len(data)

        for line in data:
            #dcmFile = '/neuro/users/chris/data/%s' % line
            dcmFile = '/neuro/users/nicolas.charlet/ChrisDbTest/%s' % line
            t = line
            t_l = t.split('/')
            t_l[4] = 'meta.json'
            nline = '/'.join(t_l)

            #metaFile = '/neuro/users/chris/data/%s' % nline
            metaFile = '/neuro/users/nicolas.charlet/ChrisDbTest/%s' % nline

            print(dcmFile)
            print(metaFile)
            b_metaFileExists = False

################################################################################
# here we read each dicoms with pydicom and each metaFile as json file.
# then we test if Series, study or patient allready exists.
################################################################################

            ds = pydicom.read_file(dcmFile)

            try:
                with open(metaFile) as meta:
                    data = json.load(meta)
                    b_metaFileExists = True
            except:
                print('no .json detected')
                pass

            test_SeriesInstanceUID=str(ds.SeriesInstanceUID)
            test_StudyInstanceUID=str(ds.StudyInstanceUID)
            test_PatientID=str(ds.PatientID)

            search1 = Series.objects.all().filter(SeriesInstanceUID=test_SeriesInstanceUID)
            #print(search1)

            search2 = Study.objects.all().filter(StudyInstanceUID=test_StudyInstanceUID)
            #print(search2)

            search3 = Patient.objects.all().filter(PatientID=test_PatientID)
            #print(search3)

################################################################################
# the first search is the case where the series allready exist, if it exist
# we don't add this series in the data base.
################################################################################

            if search1.exists():
                print('series already exists')
                #on fait rien, la SeriesInstanceUID existe deja


                for line in data:

                    UserID = data[line]['uid']
                    GroupId = data[line]['gid']
                    test_uid = UserID
                    test_gid = GroupId
                    print(test_uid)
                    print(test_gid)

################################################################################
# now we test if user are allready linked to this series or not.
# then if it exist we check if the group is link to the user and if it exist
# allready.
################################################################################

                    searchSUser = Series.objects.filter(user__UserID__startswith=test_uid)
                    # print('user id:')
                    # print(searchSUser)
                    searchUser = User.objects.all().filter(UserID=test_uid)
                    searchUGroup = User.objects.filter(group__GroupId__startswith=test_gid)
                    searchGroup = Group.objects.all().filter(GroupId=test_gid)

                    if searchUser.exists():

                        if searchSUser.exists():
                            print('user already in the series')

                        else:
                            search1.first().user.add(searchUser.first())
                            print('user added')

                        if searchUGroup.exists():
                            #print("user & group exist ")
                            print('user already in the data base')

                        else:
                            if searchGroup.exists():
                                #print("user & group exist but user not in that group")

                                searchUser.first().group.add(searchGroup.first())

                            else:

                                #print("user exist but not group")

                                ####################### Group table ######################
                                try:
                                    GroupName = data[line]['groupname']
                                except NameError:
                                    GroupName = 'undefined'
                                except AttributeError:
                                    GroupName = 'undefined'

                                try:
                                    GroupId = data[line]['gid']
                                except NameError:
                                    GroupId = 'undefined'
                                except AttributeError:
                                    GroupId = 'undefined'

                                try:
                                    GroupProject = data[line]['project']
                                except NameError:
                                    GroupProject = 'undefined'
                                except AttributeError:
                                    GroupProject = 'undefined'

                                gr=Group.objects.create(GroupName=GroupName,GroupId=GroupId,Project=Project)
                                gr.save()

                                searchUser.first().group.add(gr)


                    else:
                        #print("new user & new group")

                        ####################### Group table ######################
                        if searchGroup.exists():
                            #print("user not exist & group exist")

                            ####################### User table ######################
                            try:
                                UserName = data[line]['username']
                            except NameError:
                                UserName = 'undefined'
                            except AttributeError:
                                UserName = 'undefined'

                            try:
                                RealName = data[line]['username']
                            except NameError:
                                RealName = 'undefined'
                            except AttributeError:
                                RealName = 'undefined'

                            try:
                                UserID = data[line]['uid']
                            except NameError:
                                UserID = 'undefined'
                            except AttributeError:
                                UserID = 'undefined'

                            try:
                                Email = data[line]['email']
                            except NameError:
                                Email = 'undefined'
                            except AttributeError:
                                Email = 'undefined'

                            user=User.objects.create(UserName=UserName,RealName=RealName,
                                                     UserID=UserID,Email=Email)
                            user.save()


                            user.group.add(searchGroup.first())
                            search1.first().user.add(user)


                        else:

                            ####################### Group table ######################
                            try:
                                GroupName = data[line]['groupname']
                            except NameError:
                                GroupName = 'undefined'
                            except AttributeError:
                                GroupName = 'undefined'

                            try:
                                GroupId = data[line]['gid']
                            except NameError:
                                GroupId = 'undefined'
                            except AttributeError:
                                GroupId = 'undefined'

                            try:
                                GroupProject = data[line]['project']
                            except NameError:
                                GroupProject = 'undefined'
                            except AttributeError:
                                GroupProject = 'undefined'

                            gr=Group.objects.create(GroupName=GroupName,GroupId=GroupId,GroupProject=GroupProject)
                            gr.save()

                            #print("group")

                            ####################### User table ######################
                            try:
                                UserName = data[line]['username']
                            except NameError:
                                UserName = 'undefined'
                            except AttributeError:
                                UserName = 'undefined'

                            try:
                                RealName = data[line]['username']
                            except NameError:
                                RealName = 'undefined'
                            except AttributeError:
                                RealName = 'undefined'

                            try:
                                UserID = data[line]['uid']
                            except NameError:
                                UserID = 'undefined'
                            except AttributeError:
                                UserID = 'undefined'

                            try:
                                Email = data[line]['email']
                            except NameError:
                                Email = 'undefined'
                            except AttributeError:
                                Email = 'undefined'

                            user=User.objects.create(UserName=UserName,RealName=RealName,
                                                     UserID=UserID,Email=Email)
                            user.save()
                            user.group.add(gr)
                            search1.first().user.add(User)
                            #print("end")

################################################################################
# this case is when the study allready exist so we don't create the same study
# and patient twice.
# Compare to the first case we don't check if the user is allready link to the
# series, we just link then directly.
################################################################################

            elif search2.exists():

                ####################### Series table ######################
                try:
                  SeriesNumber=ds.SeriesNumber
                except NameError:
                  SeriesNumber = 'undefined'
                except AttributeError:
                  SeriesNumber = 'undefined'

                try:
                  SeriesInstanceUID=str(ds.SeriesInstanceUID)
                except NameError:
                  SeriesInstanceUID = 'undefined'
                except AttributeError:
                  SeriesInstanceUID = 'undefined'

                try:
                  ProtocolName=ds.ProtocolName
                except NameError:
                  ProtocolName = 'undefined'
                except AttributeError:
                  ProtocolName = 'undefined'

                try:
                  Modality=ds.Modality
                except NameError:
                  Modality = 'undefined'
                except AttributeError:
                  Modality = 'undefined'

                try:
                  SeriesDescription=ds.SeriesDescription
                except NameError:
                  SeriesDescription = 'undefined'
                except AttributeError:
                  SeriesDescription = 'undefined'

                try:
                  SeriesTime=ds.SeriesTime
                except NameError:
                  SeriesTime = 'undefined'
                except AttributeError:
                  SeriesTime = 'undefined'

                try:
                  ContrastAgent=ds.ContrastAgent
                except NameError:
                  ContrastAgent = 'undefined'
                except AttributeError:
                  ContrastAgent = 'undefined'

                try:
                  ScanningSequence=ds.ScanningSequence
                except NameError:
                  ScanningSequence = 'undefined'
                except AttributeError:
                  ScanningSequence = 'undefined'

                try:
                  BodyPartExaminated=ds.BodyPartExaminated
                except NameError:
                  BodyPartExaminated = 'undefined'
                except AttributeError:
                  BodyPartExaminated = 'undefined'

                try:
                  AcquisitionNumber=ds.AcquisitionNumber
                except NameError:
                  AcquisitionNumber = 'undefined'
                except AttributeError:
                  AcquisitionNumber = 'undefined'


                b3=Series(SeriesNumber=SeriesNumber,SeriesInstanceUID=SeriesInstanceUID,ProtocolName=ProtocolName,Modality=Modality,
                          SeriesDescription=SeriesDescription,SeriesTime=SeriesTime,ContrastAgent=ContrastAgent,ScanningSequence=ScanningSequence,
                          BodyPartExaminated=BodyPartExaminated,AcquisitionNumber=AcquisitionNumber,study=search2.first())
                b3.save()

                # group and user table

                for line in data:

                    UserID = data[line]['uid']
                    GroupId = data[line]['gid']
                    test_uid = UserID
                    test_gid = GroupId
                    print(test_uid)
                    print(test_gid)

                    searchUser = User.objects.all().filter(UserID=test_uid)
                    searchUGroup = User.objects.filter(group__GroupId__startswith=test_gid)
                    searchGroup = Group.objects.all().filter(GroupId=test_gid)

                    if searchUser.exists():

                        b3.user.add(searchUser.first())

                        if searchUGroup.exists():
                            #print("user & group exist ")
                            print('user already in the data base')

                        else:
                            if searchGroup.exists():
                                #print("user & group exist but user not in that group")

                                searchUser.first().group.add(searchGroup.first())

                            else:

                                #print("user exist but not group")

                                ####################### Group table ######################
                                try:
                                    GroupName = data[line]['groupname']
                                except NameError:
                                    GroupName = 'undefined'
                                except AttributeError:
                                    GroupName = 'undefined'

                                try:
                                    GroupId = data[line]['gid']
                                except NameError:
                                    GroupId = 'undefined'
                                except AttributeError:
                                    GroupId = 'undefined'

                                try:
                                    GroupProject = data[line]['project']
                                except NameError:
                                    GroupProject = 'undefined'
                                except AttributeError:
                                    GroupProject = 'undefined'

                                gr=Group.objects.create(GroupName=GroupName,GroupId=GroupId,Project=Project)
                                gr.save()

                                searchUser.first().group.add(gr)


                    else:
                        #print("new user & new group")

                        ####################### Group table ######################
                        if searchGroup.exists():
                            #print("user not exist & group exist")

                            ####################### User table ######################
                            try:
                                UserName = data[line]['username']
                            except NameError:
                                UserName = 'undefined'
                            except AttributeError:
                                UserName = 'undefined'

                            try:
                                RealName = data[line]['username']
                            except NameError:
                                RealName = 'undefined'
                            except AttributeError:
                                RealName = 'undefined'

                            try:
                                UserID = data[line]['uid']
                            except NameError:
                                UserID = 'undefined'
                            except AttributeError:
                                UserID = 'undefined'

                            try:
                                Email = data[line]['email']
                            except NameError:
                                Email = 'undefined'
                            except AttributeError:
                                Email = 'undefined'

                            user=User.objects.create(UserName=UserName,RealName=RealName,
                                                     UserID=UserID,Email=Email)
                            user.save()

                            user.group.add(searchGroup.first())
                            b3.user.add(user)


                        else:

                            ####################### Group table ######################
                            try:
                                GroupName = data[line]['groupname']
                            except NameError:
                                GroupName = 'undefined'
                            except AttributeError:
                                GroupName = 'undefined'

                            try:
                                GroupId = data[line]['gid']
                            except NameError:
                                GroupId = 'undefined'
                            except AttributeError:
                                GroupId = 'undefined'

                            try:
                                GroupProject = data[line]['project']
                            except NameError:
                                GroupProject = 'undefined'
                            except AttributeError:
                                GroupProject = 'undefined'

                            gr=Group.objects.create(GroupName=GroupName,GroupId=GroupId,GroupProject=GroupProject)
                            gr.save()

                            #print("group")

                            ####################### User table ######################
                            try:
                                UserName = data[line]['username']
                            except NameError:
                                UserName = 'undefined'
                            except AttributeError:
                                UserName = 'undefined'

                            try:
                                RealName = data[line]['username']
                            except NameError:
                                RealName = 'undefined'
                            except AttributeError:
                                RealName = 'undefined'

                            try:
                                UserID = data[line]['uid']
                            except NameError:
                                UserID = 'undefined'
                            except AttributeError:
                                UserID = 'undefined'

                            try:
                                Email = data[line]['email']
                            except NameError:
                                Email = 'undefined'
                            except AttributeError:
                                Email = 'undefined'

                            user=User.objects.create(UserName=UserName,RealName=RealName,
                                                     UserID=UserID,Email=Email)
                            user.save()
                            user.group.add(gr)
                            b3.user.add(user)
                            #print("end")


                ############ MR_Params table ##############
                try:
                  PixelSpacing=ds.PixelSpacing
                except NameError:
                  PixelSpacing = 'undefined'
                except AttributeError:
                  PixelSpacing = 'undefined'

                try:
                  SliceThickness=ds.SliceThickness
                except NameError:
                  SliceThickness = 'undefined'
                except AttributeError:
                  SliceThickness = 'undefined'

                try:
                  EchoTime=ds.EchoTime
                except NameError:
                  EchoTime = 'undefined'
                except AttributeError:
                  EchoTime = 'undefined'

                try:
                  EchoNumbers=ds.EchoNumbers
                except NameError:
                  EchoNumbers = 'undefined'
                except AttributeError:
                  EchoNumbers = 'undefined'

                try:
                  InversionTime=ds.InversionTime
                except NameError:
                  InversionTime = 'undefined'
                except AttributeError:
                  InversionTime = 'undefined'

                try:
                  RepetitionTime=ds.RepetitionTime
                except NameError:
                  RepetitionTime = 'undefined'
                except AttributeError:
                  RepetitionTime = 'undefined'


                b4=MR_Params(PixelSpacing=PixelSpacing,SliceThickness=SliceThickness,EchoTime=EchoTime,EchoNumbers=EchoNumbers,
                             InversionTime=InversionTime,RepetitionTime=RepetitionTime,
                             modality_params= b3)

                b4.save()

                ############# US_Params ###############
                try:
                  Name=ds.Name
                except NameError:
                  Name = 'undefined'
                except AttributeError:
                  Name = 'undefined'


                b5=US_Params(Name=Name,modality_params=b3)
                b5.save()

                ################ CT_Params ####################
                try:
                  Name=ds.Name
                except NameError:
                  Name = 'undefined'
                except AttributeError:
                  Name = 'undefined'


                b6=CT_Params(Name=Name,modality_params=b3)
                b6.save()


################################################################################
# this case is when the patient allready existe so we just create other tables
# to avoid having the same patient twice.
# for the user and group it is the same the previous case.
################################################################################

            elif search3.exists():

                ################## Study table ####################
                try:
                  StudyDescription=ds.StudyDescription
                except NameError:
                  StudyDescription = 'undefined'
                except AttributeError:
                  StudyDescription = 'undefined'

                try:
                  StationName=ds.StationName
                except NameError:
                  StationName = 'undefined'
                except AttributeError:
                  StationName = 'undefined'

                try:
                  ManufacturerModelName=ds.ManufacturerModelName
                except NameError:
                  ManufacturerModelName = 'undefined'
                except AttributeError:
                  ManufacturerModelName = 'undefined'

                try:
                  StudyInstanceUID=str(ds.StudyInstanceUID)
                except NameError:
                  StudyInstanceUID = 'undefined'
                except AttributeError:
                  StudyInstanceUID = 'undefined'

                try:
                  Pathology=ds.Pathology
                except NameError:
                  Pathology = 'undefined'
                except AttributeError:
                  Pathology = 'undefined'

                try:
                  StudyDate=ds.StudyDate
                except NameError:
                  StudyDate = 'undefined'
                except AttributeError:
                  StudyDate = 'undefined'

                try:
                  StudyTime=ds.StudyTime
                except NameError:
                  StudyTime = 'undefined'
                except AttributeError:
                  StudyTime = 'undefined'

                try:
                  AccessionNumber=ds.AccessionNumber
                except NameError:
                  AccessionNumber = 'undefined'
                except AttributeError:
                  AccessionNumber = 'undefined'

                try:
                  InstitutionName=ds.InstitutionName
                except NameError:
                  InstitutionName = 'undefined'
                except AttributeError:
                  InstitutionName = 'undefined'


                try:
                  ReferringPhysicianName=ds.ReferringPhysicianName
                except NameError:
                  ReferringPhysicianName = 'undefined'
                except AttributeError:
                  ReferringPhysicianName = 'undefined'

                try:
                  PerformingPhysicianName=ds.PerformingPhysicianName
                except NameError:
                  PerformingPhysicianName = 'undefined'
                except AttributeError:
                  PerformingPhysicianName = 'undefined'

                try:
                  ModalitiesInStudy=ds.ModalitiesInStudy
                except NameError:
                  ModalitiesInStudy = 'undefined'
                except AttributeError:
                  ModalitiesInStudy = 'undefined'

                try:
                  MagneticFieldStrength=ds.MagneticFieldStrength
                except NameError:
                  MagneticFieldStrength = 0
                except AttributeError:
                  MagneticFieldStrength = 0


                b2=Study(StudyDescription=StudyDescription,StationName=StationName,ManufacturerModelName=ManufacturerModelName,
                         StudyInstanceUID=StudyInstanceUID,Pathology=Pathology,StudyDate=StudyDate,
                         StudyTime=StudyTime,AccessionNumber=AccessionNumber,InstitutionName=InstitutionName,
                         ReferringPhysicianName=ReferringPhysicianName,ModalitiesInStudy=ModalitiesInStudy,
                         MagneticFieldStrength=MagneticFieldStrength,patient=search3.first())
                b2.save()

                ####################### Series table ######################
                try:
                  SeriesNumber=ds.SeriesNumber
                except NameError:
                  SeriesNumber = 'undefined'
                except AttributeError:
                  SeriesNumber = 'undefined'

                try:
                  SeriesInstanceUID=str(ds.SeriesInstanceUID)
                except NameError:
                  SeriesInstanceUID = 'undefined'
                except AttributeError:
                  SeriesInstanceUID = 'undefined'

                try:
                  ProtocolName=ds.ProtocolName
                except NameError:
                  ProtocolName = 'undefined'
                except AttributeError:
                  ProtocolName = 'undefined'

                try:
                  Modality=ds.Modality
                except NameError:
                  Modality = 'undefined'
                except AttributeError:
                  Modality = 'undefined'

                try:
                  SeriesDescription=ds.SeriesDescription
                except NameError:
                  SeriesDescription = 'undefined'
                except AttributeError:
                  SeriesDescription = 'undefined'

                try:
                  SeriesTime=ds.SeriesTime
                except NameError:
                  SeriesTime = 'undefined'
                except AttributeError:
                  SeriesTime = 'undefined'

                try:
                  ContrastAgent=ds.ContrastAgent
                except NameError:
                  ContrastAgent = 'undefined'
                except AttributeError:
                  ContrastAgent = 'undefined'

                try:
                  ScanningSequence=ds.ScanningSequence
                except NameError:
                  ScanningSequence = 'undefined'
                except AttributeError:
                  ScanningSequence = 'undefined'

                try:
                  BodyPartExaminated=ds.BodyPartExaminated
                except NameError:
                  BodyPartExaminated = 'undefined'
                except AttributeError:
                  BodyPartExaminated = 'undefined'

                try:
                  AcquisitionNumber=ds.AcquisitionNumber
                except NameError:
                  AcquisitionNumber = 'undefined'
                except AttributeError:
                  AcquisitionNumber = 'undefined'


                b3=Series(SeriesNumber=SeriesNumber,SeriesInstanceUID=SeriesInstanceUID,ProtocolName=ProtocolName,Modality=Modality,
                          SeriesDescription=SeriesDescription,SeriesTime=SeriesTime,ContrastAgent=ContrastAgent,ScanningSequence=ScanningSequence,
                          BodyPartExaminated=BodyPartExaminated,AcquisitionNumber=AcquisitionNumber,study=search2.first())
                b3.save()

                # group and user
                for line in data:

                    UserID = data[line]['uid']
                    GroupId = data[line]['gid']
                    test_uid = UserID
                    test_gid = GroupId
                    print(test_uid)
                    print(test_gid)

                    searchUser = User.objects.all().filter(UserID=test_uid)
                    searchUGroup = User.objects.filter(group__GroupId__startswith=test_gid)
                    searchGroup = Group.objects.all().filter(GroupId=test_gid)
                    #searchSUser = Series.objects.filter(user__GroupId__startswith=)


                    if searchUser.exists():

                        b3.user.add(searchUser.first())

                        if searchUGroup.exists():
                            #print("user & group exist ")
                            print('user already in the data base')

                        else:
                            if searchGroup.exists():
                                #print("user & group exist but user not in that group")

                                searchUser.first().group.add(searchGroup.first())

                            else:

                                #print("user exist but not group")

                                ####################### Group table ######################
                                try:
                                    GroupName = data[line]['groupname']
                                except NameError:
                                    GroupName = 'undefined'
                                except AttributeError:
                                    GroupName = 'undefined'

                                try:
                                    GroupId = data[line]['gid']
                                except NameError:
                                    GroupId = 'undefined'
                                except AttributeError:
                                    GroupId = 'undefined'

                                try:
                                    GroupProject = data[line]['project']
                                except NameError:
                                    GroupProject = 'undefined'
                                except AttributeError:
                                    GroupProject = 'undefined'

                                gr=Group.objects.create(GroupName=GroupName,GroupId=GroupId,Project=Project)
                                gr.save()

                                searchUser.first().group.add(gr)


                    else:
                        #print("new user & new group")

                        ####################### Group table ######################
                        if searchGroup.exists():
                            #print("user not exist & group exist")

                            ####################### User table ######################
                            try:
                                UserName = data[line]['username']
                            except NameError:
                                UserName = 'undefined'
                            except AttributeError:
                                UserName = 'undefined'

                            try:
                                RealName = data[line]['username']
                            except NameError:
                                RealName = 'undefined'
                            except AttributeError:
                                RealName = 'undefined'

                            try:
                                UserID = data[line]['uid']
                            except NameError:
                                UserID = 'undefined'
                            except AttributeError:
                                UserID = 'undefined'

                            try:
                                Email = data[line]['email']
                            except NameError:
                                Email = 'undefined'
                            except AttributeError:
                                Email = 'undefined'

                            user=User.objects.create(UserName=UserName,RealName=RealName,
                                                     UserID=UserID,Email=Email)
                            user.save()


                            user.group.add(searchGroup.first())
                            b3.user.add(user)


                        else:

                            ####################### Group table ######################
                            try:
                                GroupName = data[line]['groupname']
                            except NameError:
                                GroupName = 'undefined'
                            except AttributeError:
                                GroupName = 'undefined'

                            try:
                                GroupId = data[line]['gid']
                            except NameError:
                                GroupId = 'undefined'
                            except AttributeError:
                                GroupId = 'undefined'

                            try:
                                GroupProject = data[line]['project']
                            except NameError:
                                GroupProject = 'undefined'
                            except AttributeError:
                                GroupProject = 'undefined'

                            gr=Group.objects.create(GroupName=GroupName,GroupId=GroupId,GroupProject=GroupProject)
                            gr.save()

                            #print("group")

                            ####################### User table ######################
                            try:
                                UserName = data[line]['username']
                            except NameError:
                                UserName = 'undefined'
                            except AttributeError:
                                UserName = 'undefined'

                            try:
                                RealName = data[line]['username']
                            except NameError:
                                RealName = 'undefined'
                            except AttributeError:
                                RealName = 'undefined'

                            try:
                                UserID = data[line]['uid']
                            except NameError:
                                UserID = 'undefined'
                            except AttributeError:
                                UserID = 'undefined'

                            try:
                                Email = data[line]['email']
                            except NameError:
                                Email = 'undefined'
                            except AttributeError:
                                Email = 'undefined'

                            user=User.objects.create(UserName=UserName,RealName=RealName,
                                                     UserID=UserID,Email=Email)
                            user.save()
                            user.group.add(gr)
                            b3.user.add(user)
                            #print("end")

                ############ MR_Params table ##############
                try:
                  PixelSpacing=ds.PixelSpacing
                except NameError:
                  PixelSpacing = 'undefined'
                except AttributeError:
                  PixelSpacing = 'undefined'

                try:
                  SliceThickness=ds.SliceThickness
                except NameError:
                  SliceThickness = 'undefined'
                except AttributeError:
                  SliceThickness = 'undefined'

                try:
                  EchoTime=ds.EchoTime
                except NameError:
                  EchoTime = 'undefined'
                except AttributeError:
                  EchoTime = 'undefined'

                try:
                  EchoNumbers=ds.EchoNumbers
                except NameError:
                  EchoNumbers = 'undefined'
                except AttributeError:
                  EchoNumbers = 'undefined'

                try:
                  InversionTime=ds.InversionTime
                except NameError:
                  InversionTime = 'undefined'
                except AttributeError:
                  InversionTime = 'undefined'

                try:
                  RepetitionTime=ds.RepetitionTime
                except NameError:
                  RepetitionTime = 'undefined'
                except AttributeError:
                  RepetitionTime = 'undefined'


                b4=MR_Params(PixelSpacing=PixelSpacing,SliceThickness=SliceThickness,EchoTime=EchoTime,EchoNumbers=EchoNumbers,
                             InversionTime=InversionTime,RepetitionTime=RepetitionTime,
                             modality_params= b3)

                b4.save()

                ############# US_Params ###############
                try:
                  Name=ds.Name
                except NameError:
                  Name = 'undefined'
                except AttributeError:
                  Name = 'undefined'

                b5=US_Params(Name=Name,modality_params=b3)
                b5.save()

                ################ CT_Params ####################
                try:
                  Name=ds.Name
                except NameError:
                  Name = 'undefined'
                except AttributeError:
                  Name = 'undefined'

                b6=CT_Params(Name=Name,modality_params=b3)
                b6.save()

################################################################################
# this case is when we have to create each tables
# for the user and group it is the same the previous case.
################################################################################

            else:

                ################# Patient table ###################
                try:
                  PatientID=ds.PatientID
                except NameError:
                  PatientID = 'undefined'
                except AttributeError:
                  PatientID = 'undefined'

                try:
                  PatientName=ds.PatientName
                except NameError:
                  PatientName = 'undefined'
                except AttributeError:
                  PatientName = 'undefined'

                try:
                  PatientAge=ds.PatientAge
                except NameError:
                  PatientAge = 'undefined'
                except AttributeError:
                  PatientAge = 'undefined'

                try:
                  PatientSex=ds.PatientSex
                except NameError:
                  PatientSex = 'undefined'
                except AttributeError:
                  PatientSex = 'undefined'

                try:
                  PatientBirthDate=ds.PatientBirthDate
                except NameError:
                  PatientBirthDate = 'undefined'
                except AttributeError:
                  PatientBirthDate = 'undefined'

                try:
                  PatientBirthTime=ds.PatientBirthTime
                except NameError:
                  PatientBirthTime = 'undefined'
                except AttributeError:
                  PatientBirthTime = 'undefined'


                b1=Patient(PatientID=PatientID, PatientAge=PatientAge, PatientSex=PatientSex,PatientName=PatientName,
                           PatientBirthDate=PatientBirthDate, PatientBirthTime=PatientBirthTime)
                b1.save()

                ################## Study table ####################
                try:
                  StudyDescription=ds.StudyDescription
                except NameError:
                  StudyDescription = 'undefined'
                except AttributeError:
                  StudyDescription = 'undefined'

                try:
                  StationName=ds.StationName
                except NameError:
                  StationName = 'undefined'
                except AttributeError:
                  StationName = 'undefined'

                try:
                  ManufacturerModelName=ds.ManufacturerModelName
                except NameError:
                  ManufacturerModelName = 'undefined'
                except AttributeError:
                  ManufacturerModelName = 'undefined'

                try:
                  StudyInstanceUID=str(ds.StudyInstanceUID)
                except NameError:
                  StudyInstanceUID = 'undefined'
                except AttributeError:
                  StudyInstanceUID = 'undefined'

                try:
                  Pathology=ds.Pathology
                except NameError:
                  Pathology = 'undefined'
                except AttributeError:
                  Pathology = 'undefined'

                try:
                  StudyDate=ds.StudyDate
                except NameError:
                  StudyDate = 'undefined'
                except AttributeError:
                  StudyDate = 'undefined'

                try:
                  StudyTime=ds.StudyTime
                except NameError:
                  StudyTime = 'undefined'
                except AttributeError:
                  StudyTime = 'undefined'

                try:
                  AccessionNumber=ds.AccessionNumber
                except NameError:
                  AccessionNumber = 'undefined'
                except AttributeError:
                  AccessionNumber = 'undefined'

                try:
                  InstitutionName=ds.InstitutionName
                except NameError:
                  InstitutionName = 'undefined'
                except AttributeError:
                  InstitutionName = 'undefined'

                try:
                  ReferringPhysicianName=ds.ReferringPhysicianName
                except NameError:
                  ReferringPhysicianName = 'undefined'
                except AttributeError:
                  ReferringPhysicianName = 'undefined'

                try:
                  PerformingPhysicianName=ds.PerformingPhysicianName
                except NameError:
                  PerformingPhysicianName = 'undefined'
                except AttributeError:
                  PerformingPhysicianName = 'undefined'

                try:
                  ModalitiesInStudy=ds.ModalitiesInStudy
                except NameError:
                  ModalitiesInStudy = 'undefined'
                except AttributeError:
                  ModalitiesInStudy = 'undefined'

                try:
                  MagneticFieldStrength=ds.MagneticFieldStrength
                except NameError:
                  MagneticFieldStrength = 0
                except AttributeError:
                  MagneticFieldStrength = 0


                b2=Study(StudyDescription=StudyDescription,StationName=StationName,ManufacturerModelName=ManufacturerModelName,
                         StudyInstanceUID=StudyInstanceUID,Pathology=Pathology,StudyDate=StudyDate,
                         StudyTime=StudyTime,AccessionNumber=AccessionNumber,InstitutionName=InstitutionName,
                         ReferringPhysicianName=ReferringPhysicianName,ModalitiesInStudy=ModalitiesInStudy,
                         MagneticFieldStrength=MagneticFieldStrength,patient=b1)
                b2.save()

                ####################### Series table ######################
                try:
                  SeriesNumber=ds.SeriesNumber
                except NameError:
                  SeriesNumber = 'undefined'
                except AttributeError:
                  SeriesNumber = 'undefined'

                try:
                  SeriesInstanceUID=str(ds.SeriesInstanceUID)
                except NameError:
                  SeriesInstanceUID = 'undefined'
                except AttributeError:
                  SeriesInstanceUID = 'undefined'

                try:
                  ProtocolName=ds.ProtocolName
                except NameError:
                  ProtocolName = 'undefined'
                except AttributeError:
                  ProtocolName = 'undefined'

                try:
                  Modality=ds.Modality
                except NameError:
                  Modality = 'undefined'
                except AttributeError:
                  Modality = 'undefined'

                try:
                  SeriesDescription=ds.SeriesDescription
                except NameError:
                  SeriesDescription = 'undefined'
                except AttributeError:
                  SeriesDescription = 'undefined'

                try:
                  SeriesTime=ds.SeriesTime
                except NameError:
                  SeriesTime = 'undefined'
                except AttributeError:
                  SeriesTime = 'undefined'

                try:
                  ContrastAgent=ds.ContrastAgent
                except NameError:
                  ContrastAgent = 'undefined'
                except AttributeError:
                  ContrastAgent = 'undefined'

                try:
                  ScanningSequence=ds.ScanningSequence
                except NameError:
                  ScanningSequence = 'undefined'
                except AttributeError:
                  ScanningSequence = 'undefined'

                try:
                  BodyPartExaminated=ds.BodyPartExaminated
                except NameError:
                  BodyPartExaminated = 'undefined'
                except AttributeError:
                  BodyPartExaminated = 'undefined'

                try:
                  AcquisitionNumber=ds.AcquisitionNumber
                except NameError:
                  AcquisitionNumber = 'undefined'
                except AttributeError:
                  AcquisitionNumber = 'undefined'


                b3=Series(SeriesNumber=SeriesNumber,SeriesInstanceUID=SeriesInstanceUID,ProtocolName=ProtocolName,Modality=Modality,
                          SeriesDescription=SeriesDescription,SeriesTime=SeriesTime,ContrastAgent=ContrastAgent,ScanningSequence=ScanningSequence,
                          BodyPartExaminated=BodyPartExaminated,AcquisitionNumber=AcquisitionNumber,study=b2)
                b3.save()

                #group and user
                for line in data:

                    UserID = data[line]['uid']
                    GroupId = data[line]['gid']
                    test_uid = UserID
                    test_gid = GroupId
                    print(test_uid)
                    print(test_gid)

                    searchUser = User.objects.all().filter(UserID=test_uid)
                    searchUGroup = User.objects.filter(group__GroupId__startswith=test_gid)
                    searchGroup = Group.objects.all().filter(GroupId=test_gid)
                    #searchSUser = Series.objects.filter(user__GroupId__startswith=)


                    if searchUser.exists():

                        b3.user.add(searchUser.first())

                        if searchUGroup.exists():
                            #print("user & group exist ")
                            print('user already in the data base')

                        else:
                            if searchGroup.exists():
                                #print("user & group exist but user not in that group")

                                searchUser.first().group.add(searchGroup.first())

                            else:

                                #print("user exist but not group")

                                ####################### Group table ######################
                                try:
                                    GroupName = data[line]['groupname']
                                except NameError:
                                    GroupName = 'undefined'
                                except AttributeError:
                                    GroupName = 'undefined'

                                try:
                                    GroupId = data[line]['gid']
                                except NameError:
                                    GroupId = 'undefined'
                                except AttributeError:
                                    GroupId = 'undefined'

                                try:
                                    GroupProject = data[line]['project']
                                except NameError:
                                    GroupProject = 'undefined'
                                except AttributeError:
                                    GroupProject = 'undefined'

                                gr=Group.objects.create(GroupName=GroupName,GroupId=GroupId,Project=Project)
                                gr.save()

                                searchUser.first().group.add(gr)


                    else:
                        #print("new user & new group")

                        ####################### Group table ######################
                        if searchGroup.exists():
                            #print("user not exist & group exist")

                            ####################### User table ######################
                            try:
                                UserName = data[line]['username']
                            except NameError:
                                UserName = 'undefined'
                            except AttributeError:
                                UserName = 'undefined'

                            try:
                                RealName = data[line]['username']
                            except NameError:
                                RealName = 'undefined'
                            except AttributeError:
                                RealName = 'undefined'

                            try:
                                UserID = data[line]['uid']
                            except NameError:
                                UserID = 'undefined'
                            except AttributeError:
                                UserID = 'undefined'

                            try:
                                Email = data[line]['email']
                            except NameError:
                                Email = 'undefined'
                            except AttributeError:
                                Email = 'undefined'

                            user=User.objects.create(UserName=UserName,RealName=RealName,
                                                     UserID=UserID,Email=Email)
                            user.save()


                            user.group.add(searchGroup.first())
                            b3.user.add(user)


                        else:

                            ####################### Group table ######################
                            try:
                                GroupName = data[line]['groupname']
                            except NameError:
                                GroupName = 'undefined'
                            except AttributeError:
                                GroupName = 'undefined'

                            try:
                                GroupId = data[line]['gid']
                            except NameError:
                                GroupId = 'undefined'
                            except AttributeError:
                                GroupId = 'undefined'

                            try:
                                GroupProject = data[line]['project']
                            except NameError:
                                GroupProject = 'undefined'
                            except AttributeError:
                                GroupProject = 'undefined'

                            gr=Group.objects.create(GroupName=GroupName,GroupId=GroupId,GroupProject=GroupProject)
                            gr.save()

                            #print("group")

                            ####################### User table ######################
                            try:
                                UserName = data[line]['username']
                            except NameError:
                                UserName = 'undefined'
                            except AttributeError:
                                UserName = 'undefined'

                            try:
                                RealName = data[line]['username']
                            except NameError:
                                RealName = 'undefined'
                            except AttributeError:
                                RealName = 'undefined'

                            try:
                                UserID = data[line]['uid']
                            except NameError:
                                UserID = 'undefined'
                            except AttributeError:
                                UserID = 'undefined'

                            try:
                                Email = data[line]['email']
                            except NameError:
                                Email = 'undefined'
                            except AttributeError:
                                Email = 'undefined'

                            user=User.objects.create(UserName=UserName,RealName=RealName,
                                                     UserID=UserID,Email=Email)
                            user.save()
                            user.group.add(gr)
                            b3.user.add(user)
                            #print("end")


                ############ MR_Params table ##############
                try:
                  PixelSpacing=ds.PixelSpacing
                except NameError:
                  PixelSpacing = 'undefined'
                except AttributeError:
                  PixelSpacing = 'undefined'

                try:
                  SliceThickness=ds.SliceThickness
                except NameError:
                  SliceThickness = 'undefined'
                except AttributeError:
                  SliceThickness = 'undefined'

                try:
                  EchoTime=ds.EchoTime
                except NameError:
                  EchoTime = 'undefined'
                except AttributeError:
                  EchoTime = 'undefined'

                try:
                  EchoNumbers=ds.EchoNumbers
                except NameError:
                  EchoNumbers = 'undefined'
                except AttributeError:
                  EchoNumbers = 'undefined'

                try:
                  InversionTime=ds.InversionTime
                except NameError:
                  InversionTime = 'undefined'
                except AttributeError:
                  InversionTime = 'undefined'

                try:
                  RepetitionTime=ds.RepetitionTime
                except NameError:
                  RepetitionTime = 'undefined'
                except AttributeError:
                  RepetitionTime = 'undefined'



                b4=MR_Params(PixelSpacing=PixelSpacing,SliceThickness=SliceThickness,EchoTime=EchoTime,EchoNumbers=EchoNumbers,
                             InversionTime=InversionTime,RepetitionTime=RepetitionTime,
                             modality_params= b3)

                b4.save()

                ############# US_Params ###############
                try:
                  Name=ds.Name
                except NameError:
                  Name = 'undefined'
                except AttributeError:
                  Name = 'undefined'

                b5=US_Params(Name=Name,modality_params=b3)
                b5.save()

                ################ CT_Params ####################
                try:
                  Name=ds.Name
                except NameError:
                  Name = 'undefined'
                except AttributeError:
                  Name = 'undefined'

                b6=CT_Params(Name=Name,modality_params=b3)
                b6.save()
