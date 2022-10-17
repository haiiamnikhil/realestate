from django.contrib import admin

from user.models import UserDetails, Users, UserProfileDetails, GuestUsers


admin.site.register(UserDetails)
admin.site.register(Users)
admin.site.register(UserProfileDetails)
admin.site.register(GuestUsers)