from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import User, Member, Caregiver, Address, Job, JobApplication, Appointment
from .forms import UserForm, MemberForm, CaregiverForm, AddressForm, JobForm, JobApplicationForm, AppointmentForm
# Create your views here.

def dashboard(request):
    # You can add context data to pass to the template if needed
    context = {
        # 'some_data': data,
    }
    return render(request, 'dashboard.html', context)


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})


def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_update.html', {'form': form})


def user_confirm_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})

def member_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        member_form = MemberForm(request.POST)
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            member = member_form.save(commit=False)
            member.user = user
            member.save()
            return redirect('member_list')
    else:
        user_form = UserForm()
        member_form = MemberForm()
    return render(request, 'member_create.html', {'user_form': user_form, 'member_form': member_form})


def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})


def member_update(request, user_id):
    member = get_object_or_404(Member, pk=user_id)
    user = member.user
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        member_form = MemberForm(request.POST, instance=member)
        if user_form.is_valid() and member_form.is_valid():
            user_form.save()
            member_form.save()
            return redirect('member_list')
    else:
        user_form = UserForm(instance=user)
        member_form = MemberForm(instance=member)
    return render(request, 'member_update.html', {'user_form': user_form, 'member_form': member_form, 'member': member})

def member_delete(request, user_id):
    member = get_object_or_404(Member, pk=user_id)
    if request.method == 'POST':
        member.user.delete()  # This will also delete the member due to cascade delete
        return redirect('member_list')
    return render(request, 'member_delete.html', {'member': member})



def caregiver_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        caregiver_form = CaregiverForm(request.POST)
        if user_form.is_valid() and caregiver_form.is_valid():
            user = user_form.save()
            caregiver = caregiver_form.save(commit=False)
            caregiver.user = user
            caregiver.save()
            return redirect('caregiver_list')
    else:
        user_form = UserForm()
        caregiver_form = CaregiverForm()
    return render(request, 'caregiver_create.html', {'user_form': user_form, 'caregiver_form': caregiver_form})


def caregiver_list(request):
    caregivers = Caregiver.objects.all()
    return render(request, 'caregiver_list.html', {'caregivers': caregivers})


def caregiver_update(request, user_id):
    caregiver = get_object_or_404(Caregiver, pk=user_id)
    user = caregiver.user
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        caregiver_form = CaregiverForm(request.POST, instance=caregiver)
        if user_form.is_valid() and caregiver_form.is_valid():
            user_form.save()
            caregiver_form.save()
            return redirect('caregiver_list')
    else:
        user_form = UserForm(instance=user)
        caregiver_form = CaregiverForm(instance=caregiver)
    return render(request, 'caregiver_update.html', {'user_form': user_form, 'caregiver_form': caregiver_form, 'caregiver': caregiver})

def caregiver_delete(request, user_id):
    caregiver = get_object_or_404(Caregiver, pk=user_id)
    if request.method == 'POST':
        caregiver.user.delete()
        return redirect('caregiverr_list')
    return render(request, 'caregiver_delete.html', {'caregiver': caregiver})



def address_create(request):
    if request.method == 'POST':
        member_form = MemberForm(request.POST)
        address_form = AddressForm(request.POST)
        if member_form.is_valid() and address_form.is_valid():
            member = member_form.save()
            address = address_form.save(commit=False)
            address.member = member
            address.save()
            return redirect('address_list')
    else:
        member_form = MemberForm()
        address_form = AddressForm()
    return render(request, 'address_create.html', {'member_form': member_form, 'address_form': address_form})


def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'address_list.html', {'addresses': addresses})


def address_update(request, member_user_id):
    address = get_object_or_404(Address, pk=member_user_id)
    member = address.member
    if request.method == 'POST':
        member_form = MemberForm(request.POST, instance=member)
        address_form = AddressForm(request.POST, instance=address)
        if member_form.is_valid() and address_form.is_valid():
            member_form.save()
            address_form.save()
            return redirect('address_list')
    else:
        member_form = MemberForm(instance=member)
        address_form = AddressForm(instance=address)
    return render(request, 'address_update.html', {'member_form': member_form, 'address_form': address_form, 'address': address})

def address_delete(request, member_user_id):
    address = get_object_or_404(Address, pk=member_user_id)
    if request.method == 'POST':
        address.member.delete()
        return redirect('address_list')
    return render(request, 'address_delete.html', {'address': address})



def job_create(request):
    if request.method == 'POST':
        member_form = MemberForm(request.POST)
        job_form = JobForm(request.POST)
        if member_form.is_valid() and job_form.is_valid():
            member = member_form.save()
            job = job_form.save(commit=False)
            job.member = member
            job.save()
            return redirect('job_list')
    else:
        member_form = MemberForm()
        job_form = JobForm()
    return render(request, 'job_create.html', {'member_form': member_form, 'job_form': job_form})


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})


def job_update(request, member_user_id):
    job = get_object_or_404(Job, pk=member_user_id)
    member = job.member
    if request.method == 'POST':
        member_form = MemberForm(request.POST, instance=member)
        job_form = JobForm(request.POST, instance=job)
        if member_form.is_valid() and job_form.is_valid():
            member_form.save()
            job_form.save()
            return redirect('job_list')
    else:
        member_form = MemberForm(instance=member)
        job_form = JobForm(instance=job)
    return render(request, 'job_update.html', {'member_form': member_form, 'job_form': job_form, 'job': job})

def job_delete(request, member_user_id):
    job = get_object_or_404(Job, pk=member_user_id)
    if request.method == 'POST':
        job.member.delete()
        return redirect('job_list')
    return render(request, 'job_delete.html', {'job': job})





def jobApplication_create(request):
    if request.method == 'POST':
        caregiver_form = CaregiverForm(request.POST)
        jobApplication_form = JobApplicationForm(request.POST)
        if caregiver_form.is_valid() and JobApplicationForm.is_valid():
            caregiver = caregiver_form.save()
            jobApplication = JobApplicationForm.save(commit=False)
            jobApplication.caregiver = caregiver
            jobApplication.save()
            return redirect('jobApplication_list')
    else:
        caregiver_form = CaregiverForm()
        jobApplication_form = JobApplicationForm()
    return render(request, 'jobApplication_create.html', {'caregiver_form': caregiver_form, 'jobApplication_form': jobApplication_form})


def jobApplication_list(request):
    jobApplications = JobApplication.objects.all()
    return render(request, 'jobApplication_list.html', {'jobApplications': jobApplications})


def appointment_create(request):
    if request.method == 'POST':
        caregiver_form = CaregiverForm(request.POST)
        appointment_form = AppointmentForm(request.POST)
        if caregiver_form.is_valid() and appointment_form.is_valid():
            caregiver = caregiver_form.save()
            appointment = AppointmentForm.save(commit=False)
            appointment.caregiver = caregiver
            appointment.save()
            return redirect('appointment_list')
    else:
        caregiver_form = CaregiverForm()
        appointment_form = AppointmentForm()
    return render(request, 'appointment_create.html', {'caregiver_form': caregiver_form, 'appointment_form': appointment_form})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

