from django.db import models

# Create your models here.


class Student(models.Model):
    fName = models.CharField(max_length=100, blank=False)
    lName = models.CharField(max_length=100, blank=False)
    studentId = models.IntegerField(primary_key=True)
    date_joined = models.DateField()
    # we save hash of password not the raw password
    password = models.CharField(max_length=50, blank=False)
    email = models.EmailField()
    Courses = models.ManyToManyField(Course)

    def __str__(self):
        return '{0}: {1} {2}'.format(str(self.fName), str(self.lName), str(self.studentId))

    def year(self):
        return str(self.date)[:4]


class Teacher(models.Model):
    fName = models.CharField(max_length=100, blank=False)
    lName = models.CharField(max_length=100, blank=False)
    teacherId = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return '{0}: {1} {2}'.format(str(self.fName), str(self.lName), str(self.teacherId))


class Course(models.Model):
    cName = models.CharField(max_length=100)
    credit = models.IntegerField(max_length=1, choices=(0, 1, 2, 3))

    DAY = (
        (1, 'SAT'),
        (2, 'SUN'),
        (3, 'MON'),
        (4, 'TUE'),
        (5, 'WED'),
        (6, 'SAT-MON'),
        (7, 'SUN-TUE')
    )
    day = models.IntegerField(max_length=1, choices=DAY)

    #We only define the beginning and each session lasts 1.5 hours
    TIME = ('07:45', '09:15', '10:45', '13:00', '15:00')
    time = models.IntegerField(max_length=5, choices=TIME)

    cId = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()

    teacherId = models.ForeignKey(Teacher.teacherId, on_delete=models.CASCADE)

#class Handler(models.Model):
#    cId = models.ForeignKey(Course.cId, on_delete=models.CASCADE)
#    teacherId = models.ForeignKey(Teacher.teacherId, on_delete=models.CASCADE)
#    studentId = models.ForeignKey(Student.studentId, on_delete=models.CASCADE)
