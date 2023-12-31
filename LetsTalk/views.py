from django.shortcuts import render,redirect
from .models import UserAnswers
# Create your views here.
def index(request):
    return render(request,'index.html')


def questions_page(request):
    return render(request, 'questions.html')

def submit_answers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')
        question4 = request.POST.get('question4')
        question5=  request.POST.get('question5')
        question6 = request.POST.get('question6')
        question7 = request.POST.get('question7')
        question8 = request.POST.get('question8')

        # Process and save the data to the database as needed
        # Example: Save to a PostgreSQL model
        user_answers=UserAnswers(name=name,question1=question1,question2=question2,
                                 question3=question3,question4=question4,
                                 question5=question5,question6=question6,
                                 question7=question7,question8=question8,
                                 )
        user_answers.save()
        return render(request, 'confirmation_page.html', {'name': name})
    else:
        # Handle non-POST requests as needed
        return render(request, 'questions.html')
