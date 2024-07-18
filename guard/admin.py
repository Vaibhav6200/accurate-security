from django.contrib import admin
from .models import Enrolment


class EnrolmentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'designation_applied_for', 'mobile_no_1', 'date_of_birth', 'marital_status',
        'name_of_bank', 'uan_no', 'name_of_company', 'spouse_name'
    )
    search_fields = (
        'full_name', 'mobile_no_1', 'mobile_no_2', 'aadhar_no', 'voter_id_dl_no',
        'name_of_bank', 'uan_no', 'name_of_company', 'spouse_name', 'emergency_contact_person'
    )
    list_filter = (
        'designation_applied_for', 'marital_status', 'name_of_bank', 'education_qualification'
    )
    fieldsets = (
        (None, {
            'fields': ('date', 'name_of_unit', 'designation_applied_for', 'employee_image')
        }),
        ('Personnel Details', {
            'fields': (
                'full_name', 'mother_name', 'father_name', 'present_address',
                'present_address_police_station', 'permanent_address', 'permanent_address_police_station',
                'mobile_no_1', 'mobile_no_2', 'height', 'weight', 'chest',
                'education_qualification', 'identification_mark', 'date_of_birth', 'age_as_on_date', 'marital_status'
            )
        }),
        ('Identification Details', {
            'fields': (
                'aadhar_no', 'voter_id_dl_no', 'name_of_bank', 'bank_acct_no', 'ifsc_code'
            )
        }),
        ('Previous Service Details', {
            'fields': (
                'uan_no', 'esic_ip_no', 'name_of_company', 'designation', 'from_date', 'to_date'
            )
        }),
        ('Family Details', {
            'fields': (
                'spouse_name', 'spouse_date_of_birth', 'child_1_name', 'child_2_name'
            )
        }),
        ('Emergency Contact Details', {
            'fields': (
                'emergency_contact_person', 'emergency_contact_relation', 'emergency_contact_mobile_no'
            )
        }),
    )


admin.site.register(Enrolment, EnrolmentAdmin)
