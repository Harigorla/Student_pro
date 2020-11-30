from django.db import models


class StudentRegister(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    ssc = models.CharField(max_length=50)
    inter = models.CharField(max_length=50)


class StudentApply(models.Model):
    studentregister = models.OneToOneField(StudentRegister, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    national = models.CharField(max_length=50)


class StudentList(models.Model):
    studentapply = models.ForeignKey(StudentApply, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
