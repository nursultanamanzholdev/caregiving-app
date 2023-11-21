from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    given_name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_description = models.TextField(blank=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = '"PLATFORM"."USER"'

class Caregiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='caregiver_user_id', primary_key=True)
    photo = models.BinaryField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    caregiving_type = models.CharField(max_length=50, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    commission_applied = models.BooleanField(default=False)

    class Meta:
        db_table = '"PLATFORM"."CAREGIVER"'

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='member_user_id', primary_key=True)
    house_rules = models.TextField(blank=True)

    class Meta:
        db_table = '"PLATFORM"."MEMBER"'

class Address(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, db_column='member_user_id', primary_key=True)
    house_number = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=100, blank=True)
    town = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = '"PLATFORM"."ADDRESS"'

class Job(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, db_column='member_user_id', primary_key=True)
    required_caregiving_type = models.CharField(max_length=50, blank=True)
    other_requirements = models.TextField(blank=True)
    date_posted = models.DateField()

    class Meta:
        db_table = '"PLATFORM"."JOB"'

class JobApplication(models.Model):
    caregiver = models.OneToOneField(Caregiver, on_delete=models.CASCADE, db_column='caregiver_user_id', primary_key=True)
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    date_applied = models.DateField()

    class Meta:
        db_table = '"PLATFORM"."JOB_APPLICATION"'

class Appointment(models.Model):
    caregiver = models.OneToOneField(Caregiver, on_delete=models.CASCADE, db_column='caregiver_user_id', primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_user_id')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    work_hours = models.IntegerField()
    status = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = '"PLATFORM"."APPOINTMENT"'

