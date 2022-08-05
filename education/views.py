from django.shortcuts import render
from django.core.mail import send_mail



# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        recipients=['eazikezi1999@gmail.com']
        contact = {'name':name, 'email':email, 'message':message, 'recipients':recipients}

        message = '''
        New message: {}
        From: {}
        '''.format(contact['message'], contact['email'])
        send_mail(name, message, None , recipients)
    return render(request, 'education/home.html', {})

def computing(request):
    return render(request, 'education/computing.html', {})

def business(request):
    return render(request, 'education/business.html', {})

def education(request):
    return render(request, 'education/education.html', {})

def graduation(request):
    return render(request, 'education/graduation.html', {})

def growth(request):
    return render(request, 'education/growth.html', {})

def health(request):
    return render(request, 'education/health.html', {})

def computing(request):
    return render(request, 'education/computing.html', {})

def research(request):
    return render(request, 'education/research.html', {})

def social(request):
    return render(request, 'education/social.html', {})

def theology(request):
    return render(request, 'education/theology.html', {})

def about(request):
    return render(request, 'education/about.html')



def starter(request):
    return render(request, 'education/starter.html')


def application(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        other_names = request.POST.get('other_names')
        campus = request.POST.get('campus')
        study = request.POST.get('study')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        Date_of_birth = request.POST.get('Date_of_birth')
        residence = request.POST.get('residence')
        nationality = request.POST.get('nationality')
        phone = request.POST.get('phone')
        where = request.POST.get('where')
        file1 = request.POST.get('file1')
        file2 = request.POST.get('file2')
        file3 = request.POST.get('file3')
        email = request.POST.get('email')
        other_contact = request.POST.get('other_contact')
        recipients=['eazikezi1999@gmail.com']
        applicant = {'first_name':first_name, 'other_names':other_names, 'campus':campus, 'study':study, 'course':course, 'gender':gender,
        'Date_of_birth':Date_of_birth, 'residence':residence, 'nationality':nationality, 'phone':phone,
        'where':where, 'file1':file1, 'file2':file2, 'file3':file3, 'email':email, 'other_contact':other_contact, 'recipients':recipients}
    
        message = '''
        New message: {}
        From: {}
        '''.format(applicant['first_name'], applicant['email'])
        send_mail(first_name, other_names, message, None, recipients)
    return render(request, 'education/application.html')




    




