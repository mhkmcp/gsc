from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .forms import MemberForm, CustomUserCreationForm


def index(request):
    return render(request, "pages/home.html")

# about us


def introduction(request):
    return render(request, "pages/about-us/introduction.html")


def purpose(request):
    return render(request, 'pages/about-us/purpose.html')


def president_speech(request):
    return render(request, 'pages/about-us/purpose.html')


def courtesy_speech(request):
    return render(request, 'pages/about-us/courtesy_speech.html')


# committee

def adviser(request):
    return render(request, 'pages/commiittee/adviser.html')


def management(request):
    return render(request, 'pages/commiittee/management.html')


def general(request):
    return render(request, 'pages/commiittee/general.html')


def election(request):
    return render(request, 'pages/commiittee/election.html')


# member


def requirements(request):
    return render(request, 'pages/member/requirements.html')


def how_to_be_member(request):
    return render(request, 'pages/member/how_to_be_member.html')


def admission_form(request):
    if request.method == 'POST':
        member_form = MemberForm(request.POST or None) # member form
        user_creation_form = CustomUserCreationForm(request.POST or None) # signup form

        if user_creation_form.is_valid() and member_form.is_valid():
            # create new User
            user = user_creation_form.save(commit=False)
            passport = member_form.cleaned_data.get('passport')
            username = passport[:6]
            # print(username)
            user.username = username
            user.is_active = False
            user.save()
            print(user)

            # create new Member
            member = member_form.save(commit=False)
            member.user = user
            member.save()
            return redirect('admission_form')
        else:
            print(user_creation_form.errors.as_data)
            print(member_form.errors.as_data)
    else:
        member_form = MemberForm()
        user_creation_form = CustomUserCreationForm()

    context = {
        'member_form': member_form,
        'user_form': user_creation_form
    }

    return render(request, 'pages/member/admission_form.html', context=context)


def member_list(request):
    return render(request, 'pages/member/member_list.html')


def general_member(request):
    return render(request, 'pages/member/general_member.html')


def lifetime_member(request):
    return render(request, 'pages/member/lifetime_member.html')


def honorary_member(request):
    return render(request, 'pages/member/honorary_member.html')


def member_info(request):
    return render(request, 'pages/member/member_info.html')


def member_share(request):
    return render(request, 'pages/member/member_share.html')


def collection_info(request):
    return render(request, 'pages/member/yearly_collection_info.html')


def audit_report(request):
    return render(request, 'pages/member/audit_report.html')


def blood_group_dob(request):
    return render(request, 'pages/member/dob_bg.html')

# deposit


def financial(request):
    return render(request, 'pages/deposit/financial_institute.html')


def other_way(request):
    return render(request, 'pages/deposit/other_way.html')

# development


def scholarship(request):
    return render(request, 'pages/development/scholarship.html')


def training(request):
    return render(request, 'pages/development/training.html')


def treatment(request):
    return render(request, 'pages/development/treatment.html')


# Union

def history(request):
    return render(request, 'pages/union/history.html')

def employees(request):
    return render(request, 'pages/union/employees.html')

def at_a_glance(request):
    return render(request, 'pages/union/at-a-glance.html')

def union_info(request):
    return render(request, 'pages/union/info.html')

def freedom_fighter(request):
    return render(request, 'pages/union/freedom-fighters.html')

def village(request):
    return render(request, 'pages/union/villages.html')

def principal_list(request):
    return render(request, 'pages/union/principal.html')

def institute_president_list(request):
    return render(request, 'pages/union/institute-president.html')

def hospital_commiunity_center(request):
    return render(request, 'pages/union/hospital-and-commiunity-center.html')

def institute(request):
    return render(request, 'pages/union/institutes.html')

# Union institutes

def sonatia(request):
    return render(request, 'pages/union/institute/sonatia.html')

# contact
def contact(request):
    return render(request, 'pages/contact.html')
