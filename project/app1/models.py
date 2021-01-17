from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db import models
from datetime import timedelta

# Create your models here.
time_slots = (
    ('7:30 - 8:30', '7:30 - 8:30'),
    ('8:30 - 9:30', '8:30 - 9:30'),
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('11:00 - 11:50', '11:00 - 11:50'),
    ('11:50 - 12:40', '11:50 - 12:40'),
    ('12:40 - 1:30', '12:40 - 1:30'),
)

sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Dept(models.Model):
    dept_id = models.CharField(primary_key='True', max_length=100)
    dept_name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.dept_name


class Class(models.Model):
    Dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    program_id = models.CharField(primary_key='True', max_length=100)
    program_name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.program_name


class Courses(models.Model):
    program = models.ForeignKey(Class, on_delete=models.CASCADE)
    course_id = models.CharField(primary_key='True', max_length=100)
    course_name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        cr = Courses.objects.get(course_id=self.course_id)
        return '%s' % (cr.course_name)


class Teachers(models.Model):
    Dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    teacher_id = models.CharField(primary_key='True', max_length=100)
    teacher_name = models.CharField(max_length=100)
    teacher_DOB = models.DateField(default='1980-01-01')
    objects = models.Manager()

    def __str__(self):
        return self.teacher_name



class Assign(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        cr = Courses.objects.get(course_id=self.course_id)
        te = Teachers.objects.get(teacher_id=self.teacher_id)
        return '%s : %s ' % (te.teacher_name,cr.course_id)


class AssignTime(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    period = models.CharField(max_length=50, choices=time_slots, default='11:00 - 11:50')
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK)
    objects = models.Manager()
from django.db import models

# Create your models here.
