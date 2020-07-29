from django.contrib import admin
from . models import Complaint, ComplaintImages, ReportIssue, UserAddress, Comments, UserTestimonials


admin.site.register(Complaint)
admin.site.register(ComplaintImages)
admin.site.register(ReportIssue)
admin.site.register(UserAddress)
admin.site.register(Comments)
admin.site.register(UserTestimonials)