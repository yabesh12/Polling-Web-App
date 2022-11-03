from django.shortcuts import render
from .models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

def vote(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    # if request.method == 'POST':
    #     inputvalue = request.POST['choice']
    #     selection_option = options.get(id=inputvalue)
    #     selection_option.vote += 5
    #     selection_option.save()

    return render(request, 'vote.html', {'question':question, 'options': options })

def result(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 5
        selection_option.save()
    return render(request, 'result.html', {'question': question, 'options': options})

# LOGIN
def login_user(request):
    mobile_no = request.POST.get('mobile_number')
    dob = request.POST.get('date_of_birth')

    user_obj = CustomUser.objects.filter(mobile_no=mobile_no, date_of_birth=dob)
    if user_obj.exists():
        user = user_obj.first()
        return redirect('poll')
    else:
        messages.error(request, "You are not authorized user to this POLL! You can participate once after the admin add you.") 
    return render(request, 'login.html')   