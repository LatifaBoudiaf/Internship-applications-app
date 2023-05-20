from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class University(models.Model):
    univName = models.CharField(max_length=200, primary_key=True)
    univAddress = models.CharField(max_length=255)
    univDirectorName = models.CharField(max_length=200)

    def __str__(self):
        return self.univName


class Faculty(models.Model):
    facultyID = models.CharField(max_length=20, primary_key=True)
    facultyName = models.CharField(max_length=200)
    univName = models.ForeignKey(
        University, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.facultyID


class Department(models.Model):
    depID = models.CharField(max_length=20, primary_key=True)
    depName = models.CharField(max_length=200)
    facultyID = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.depID


class Company(models.Model):
    companyID = models.CharField(max_length=20, primary_key=True)
    companyName = models.CharField(max_length=200)
    companyAddress = models.CharField(max_length=200)

    def __str__(self):
        return self.companyName


class internshipOffer(models.Model):
    publicationDate = models.DateTimeField(auto_now_add=True, null=True)
    duration = models.IntegerField()
    subject = models.CharField(max_length=200)
    offeredBy = models.ForeignKey(
        Company, null=True, on_delete=models.SET_NULL)
    startDate = models.DateField()
    endDate = models.DateField()
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.subject


class Marks(models.Model):
    MARKS = [
        ('1 Point', '1 Point'),
        ('2 Points', '2 Points'),
        ('3 Points', '3 Points'),
        ('4 Points', '4 Points')
    ]
    # studentCardNumber = models.
    # studentName = models.
    # supervisorName = models.
    ratingDate = models.DateField(auto_now_add=True)
    generalDiscipline = models.CharField(max_length=8, choices=MARKS)
    workAptitudes = models.CharField(max_length=8, choices=MARKS)
    Initiative = models.CharField(max_length=8, choices=MARKS)
    innovationAbilities = models.CharField(max_length=8, choices=MARKS)
    knowledgeAcquired = models.CharField(max_length=8, choices=MARKS)
    totalGrade = models.CharField(max_length=2)
    appreciation = models.CharField(max_length=50)

    def __str__(self):
        return self.totalGrade


class Presence(models.Model):
    internshipScheduledDay = models.DateField()
    # studentCardNumber = models.CharField(max_length=12)
    isPresent = models.BooleanField()

    def __str__(self):
        return self.internshipScheduledDay


class Notification(models.Model):
    # receiverID = models.CharField
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    supervisorName = models.CharField(max_length=200)
    companyName = models.CharField(max_length=200)
    InternshipSubject = models.CharField(max_length=200)
    studentName = models.CharField(max_length=200)
    univName = models.ForeignKey(
        University, on_delete=models.SET_NULL, null=True)
    # headOfDepartmentName = models.CharField
    internshipStartDate = models.DateField()
    internshipEndDate = models.DateField()
    certificateGivenDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.studentName


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cardNumber = models.CharField(max_length=12)
    ssn = models.CharField(max_length=12)
    yearOfStudy = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=20, blank=True)
    birthDate = models.DateField(blank=True, null=True)
    birthPlace = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Admin(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    dep = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    phoneNumber = models.CharField(max_length=20)
    fax = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.user.username


class Supervisor(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, related_name='supervisor_profile')
    phoneNumber = models.CharField(max_length=20)
    fax = models.CharField(max_length=12, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class InternshipApplication(models.Model):
    studentName = models.CharField(max_length=200)
    cardNumber = models.IntegerField()
    studentFac = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, null=True)
    studentDep = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)
    ssn = models.IntegerField()
    DIPLOMA = [
        ('Lisence', 'Lisence'),
        ('Master', 'Master')
    ]

    STATUS = [
        ('Pending', 'Pending'),
        ('Admin Approved', 'Admin Approved'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]
    diploma = models.CharField(max_length=7, choices=DIPLOMA)
    studentNumber = models.IntegerField()
    theme = models.CharField(max_length=200)
    offeredBy = models.CharField(max_length=200)
    startingDate = models.DateField()
    endingDate = models.DateField()
    duration = models.IntegerField()
    responsible = models.CharField(max_length=100)
    responsibleEmail = models.CharField(max_length=100)
    responsibleNumber = models.IntegerField()
    supervisor = models.CharField(max_length=100)
    supervisorEmail = models.CharField(max_length=100)
    supervisorNumber = models.IntegerField()
    status = models.CharField(max_length=14, choices=STATUS, default='Pending')
    applicant = models.ForeignKey(
        User, related_name='applicant', on_delete=models.SET_NULL, null=True, blank=True)
    internshipSupervisor = models.ForeignKey(
        Supervisor, related_name='internship_supervisor', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.applicant)
