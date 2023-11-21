from django import forms

from .models import User, Member, Caregiver, Address, Job, JobApplication, Appointment

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('__all__')

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('__all__')

class CaregiverForm(forms.ModelForm):
    class Meta:
        model = Caregiver
        fields = ('__all__')

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('__all__')

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('__all__')


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('__all__')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('__all__')


