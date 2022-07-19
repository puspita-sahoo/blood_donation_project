from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class BloodGroup(models.Model):
    name = models.CharField(primary_key=True,max_length=4)
    # req_sessions = models.ManyToManyField('BloodRequestSession', through='BloodGroupSessionMapper')

    def __str__(self):
        return self.name

class UserDetail(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    blood_group = models.OneToOneField(BloodGroup, on_delete=models.DO_NOTHING)
    contact_no = models.CharField(max_length=10, unique=True)
    pincode = models.IntegerField()
    image = models.ImageField(upload_to='static/images', default=True)
    is_donor = models.BooleanField(default=True)
    last_donated_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user)


class BloodRequestSession(models.Model):
    # id = models.IntegerField(primary_key=True)
    req_user = models.ForeignKey(User, on_delete=models.CASCADE)
    pincode = models.IntegerField()
    total_unit = models.PositiveIntegerField(default=1)  # 1unit = 500ml blood

    req_date = models.DateTimeField(default=timezone.now)
    till_date = models.DateTimeField(default=timezone.now)

    blood_groups = models.ManyToManyField(BloodGroup, through='BloodGroupSessionMapper',
        related_name='requests',
       
     )

    def __str__(self):
        return f"{self.req_user}_{self.blood_groups}_{self.pincode}"



class BloodGroupSessionMapper(models.Model):
   
    blood_group = models.ForeignKey( BloodGroup, on_delete=models.CASCADE, related_name='bloodgroups')
    request_session = models.ForeignKey( BloodRequestSession, on_delete=models.CASCADE, related_name='sessions')



    def __str__(self):
        return f'{self.blood_group.__str__}_{self.request_session.__str__}'


class BloodRequestStatus(models.Model):
    session = models.ForeignKey(BloodRequestSession, on_delete=models.CASCADE)
    donner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    invitation_status = models.CharField(max_length=10, default='pending')
    donation_status = models.CharField(max_length=10,default=True)
    donation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.invitation_status}_{self.donation_status}"



