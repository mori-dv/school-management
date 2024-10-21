from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    subject = models.CharField(max_length=100)
    hire_date = models.DateField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    national_ID = models.CharField(max_length=12)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    age = models.IntegerField()
    grade = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='classes')
    subject = models.CharField(max_length=100)
    class_time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = 'P', "PRESENT"
        ABSENT = 'A', "ABSENT"
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PRESENT)

    def __str__(self):
        return f"{self.student} - {self.class_name} - {self.status}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='grades')
    score = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.class_name} - {self.score}"
