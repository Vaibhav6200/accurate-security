from django.db import models


class Enrolment(models.Model):
    # Basic Information
    date = models.DateField(null=True, blank=True)
    name_of_unit = models.CharField(max_length=255, null=True, blank=True)
    designation_applied_for = models.CharField(max_length=255, null=True, blank=True)
    employee_image = models.ImageField(upload_to='images/', null=True, blank=True)

    # Personnel Details
    full_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    present_address = models.TextField(null=True, blank=True)
    present_address_police_station = models.CharField(max_length=255, null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    permanent_address_police_station = models.CharField(max_length=255, null=True, blank=True)
    mobile_no_1 = models.CharField(max_length=15)
    mobile_no_2 = models.CharField(max_length=15, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    chest = models.FloatField(null=True, blank=True)
    education_qualification = models.CharField(max_length=255, null=True, blank=True)
    identification_mark = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField()
    age_as_on_date = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=20, choices=[('Single', 'Single'), ('Married', 'Married'), ('Other', 'Other')])

    # Identification Details
    aadhar_no = models.CharField(max_length=12)
    voter_id_dl_no = models.CharField(max_length=255, null=True, blank=True)
    name_of_bank = models.CharField(max_length=255, null=True, blank=True)
    bank_acct_no = models.CharField(max_length=20, null=True, blank=True)
    ifsc_code = models.CharField(max_length=11, null=True, blank=True)

    # Previous Service Details
    uan_no = models.CharField(max_length=20, null=True, blank=True)
    esic_ip_no = models.CharField(max_length=20, null=True, blank=True)
    name_of_company = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    # Family Details
    spouse_name = models.CharField(max_length=255, null=True, blank=True)
    spouse_date_of_birth = models.DateField(null=True, blank=True)
    child_1_name = models.CharField(max_length=255, null=True, blank=True)
    child_2_name = models.CharField(max_length=255, null=True, blank=True)

    # Emergency Contact Details
    emergency_contact_person = models.CharField(max_length=255)
    emergency_contact_relation = models.CharField(max_length=255)
    emergency_contact_mobile_no = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

