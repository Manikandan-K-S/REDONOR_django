from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, auth
from .models import Donor_detail
from datetime import datetime
from django.http import JsonResponse
from django.contrib import messages


from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['mobile']
        mail = request.POST['mail']
        city = request.POST['city']
        address = request.POST['address']
        dob = request.POST['dob']
        group = request.POST['bloodgroup']
        gender = request.POST['gender']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password,
            email=mail,
            first_name=firstname,
            last_name=lastname
        )
        user.save()

        details = Donor_detail(
            user=user,
            name=firstname+' '+lastname,
            mobile=username,
            address=address,
            bloodgroup=group,
            gender=gender,
            city=city,
            dob=datetime.strptime(dob, '%Y-%m-%d').date()
        )

        details.save()

        user = auth.authenticate(username=username,
                                 password=password
                                 )

        auth.login(request, user)

        return redirect('/')

    else:
        return render(request, 'signup.html')


@csrf_exempt
def check_existing_data(request):

    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        mobile = request.POST['mobile']
        email = request.POST['email']

        data = {
            'mobile_exists': User.objects.filter(username=mobile).exists(),
            'email_exists': User.objects.filter(email=email).exists(),
        }

        return JsonResponse(data)


def login(request):

    if request.method == 'POST':
        username = request.POST['mobile']
        password = request.POST['password']
        user = auth.authenticate(username=username,
                                 password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Wrong Username and password')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def search_donor(request):
    bloodgroup = request.GET.get('bloodgroup')
    city = request.GET.get('city')

    if bloodgroup and city:
        donors = Donor_detail.objects.filter(
            bloodgroup=bloodgroup,
            city=city)

    else:
        donors = []

    return render(request, 'searchdonor.html', {'donors': donors})
