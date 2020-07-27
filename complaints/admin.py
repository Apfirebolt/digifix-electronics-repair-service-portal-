from django.contrib import admin
from . models import Complaint, ComplaintImages, ReportIssue


admin.site.register(Complaint)
admin.site.register(ComplaintImages)
admin.site.register(ReportIssue)
