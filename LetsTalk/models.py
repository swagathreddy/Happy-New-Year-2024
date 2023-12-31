from django.db import models

# Create your models here.

class UserAnswers(models.Model):
    name = models.CharField(max_length=255)
    question1 = models.TextField(default='',verbose_name="How would you describe our relationship and What do you think makes our bond unique?")
    question2 = models.TextField(default='',verbose_name="What is your favorite memory of us together?")
    question3 = models.TextField(default='',verbose_name="Are there aspects of my life or feelings that you think I may not openly express?")
    question4 = models.TextField(default='',verbose_name="What advice would you offer me when navigating tough times?")
    question5 = models.TextField(default='',verbose_name="How close am I to you so that you'll share everything with me?")
    question6 = models.TextField(default='',verbose_name="Are you proud of me?")
    question7 = models.TextField(default='',verbose_name="Are there any changes you think I could make to improve or enhance myself?")
    question8 = models.TextField(default='',verbose_name="Any suggestions for me?")
    
    
    # Add more fields for additional questions as needed

    def __str__(self):
        return f"{self.name}'s Answers"
