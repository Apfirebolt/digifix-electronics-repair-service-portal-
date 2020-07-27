from django.db import models
from digifix_computer_repair.settings import AUTH_USER_MODEL


class Complaint(models.Model):
  created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complaints_created')
  assigned_engineer = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignments')
  created_at = models.DateTimeField(auto_now=True)
  description = models.TextField()
  is_resolved = models.BooleanField(default=False)
  has_issues = models.BooleanField(default=False)

  def __repr__(self):
    return 'Description (%s, %s)' % (self.created_by.username, self.assigned_engineer.username)

  class Meta:
    verbose_name_plural = "Complaints"


class ComplaintImages(models.Model):
  related_complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='all_images')
  gadget_image = models.ImageField(upload_to='complaint_images')
  image_description = models.TextField()

  def __str__(self):
    return str(self.related_complaint.id) + ' - ' + str(self.image_description)

  class Meta:
    verbose_name_plural = "Complaint Images"


class ReportIssue(models.Model):
  related_complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='all_issues')
  description = models.TextField()
  reported_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.related_complaint.id) + ' - ' + str(self.description)

  class Meta:
    verbose_name_plural = "Complaint Issues"

