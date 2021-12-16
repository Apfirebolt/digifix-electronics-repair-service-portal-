from django.db import models
from digifix_computer_repair.settings import AUTH_USER_MODEL
from django.db.models import Q

STATUS_CHOICES = (
    ("NOT YET OPENED", "Not Yet Opened"),
    ("OPENED", "Opened"),
    ("IN PROGRESS", "In Progress"),
    ("HAS ISSUES", "Has Issues"),
    ("FIXED", "Fixed"),
)

DEVICE_TYPE_CHOICES = (
    ("DESKTOP", "Desktop"),
    ("LAPTOP", "Laptop"),
    ("Playstation", "Playstation"),
    ("Mobile", "Mobile"),
    ("Headphone", "Headphone"),
    ("Keyboard", "Keyboard"),
    ("Others", "Others"),
)

RATING_CHOICES = [(i, i) for i in range(6)]


class Complaint(models.Model):
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complaints_created')
    assigned_engineer = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                                          limit_choices_to=Q(groups__name='Engineers'), related_name='assignments',
                                          null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    is_resolved = models.BooleanField(default=False)
    has_issues = models.BooleanField(default=False)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default="Not Yet Opened")
    status_text = models.TextField('Status Text', blank=True, null=True)
    device_type = models.CharField('Device Type', max_length=100, choices=DEVICE_TYPE_CHOICES, null=True, blank=True)
    reference_id = models.CharField('Reference ID', max_length=100, null=True, blank=True)

    def __str__(self):
        return 'Description (%s, %s)' % (self.created_by.username, self.device_type)

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
    written_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='all_user_issues', null=True,
                                   blank=True)

    def __str__(self):
        return str(self.related_complaint.id) + ' - ' + str(self.description)

    class Meta:
        verbose_name_plural = "Complaint Issues"


class Comments(models.Model):
    related_complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='all_thread_comments')
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)
    written_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='all_comments', null=True,
                                   blank=True)

    def __str__(self):
        return str(self.related_complaint.id) + ' - ' + str(self.description)

    class Meta:
        verbose_name_plural = "Complaint Comments"


class UserAddress(models.Model):
    address = models.CharField(max_length=200)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='all_addresses')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return str(self.address) + ' - ' + str(self.owner.username)

    class Meta:
        verbose_name_plural = "User Addresses"


class UserTestimonials(models.Model):
    written_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_testimonial')
    content = models.TextField("Testimonial Content")
    posted_at = models.DateTimeField(auto_now=True)
    service_rating = models.IntegerField("Service Ratings", choices=RATING_CHOICES, null=True, blank=True)

    def __str__(self):
        return str(self.written_by.username) + ' - ' + str(self.content)

    class Meta:
        verbose_name_plural = "User Testimonials"
