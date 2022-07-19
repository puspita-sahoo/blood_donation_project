from django.contrib import admin
from .models import BloodGroup, UserDetail, BloodRequestSession, BloodRequestStatus
from django.contrib.auth.models import User



@admin.register(BloodGroup)
class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'contact_no', 'is_donor', 'last_donated_date')


@admin.register(BloodRequestSession)
class BloodRequestSessionAdmin(admin.ModelAdmin):
    list_display = ('req_user', 'pincode', 'total_unit', 'req_date', 'till_date')


