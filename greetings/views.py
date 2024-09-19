from django.shortcuts import render
from datetime import datetime

def greet_user(request):
    current_time = datetime.now().time()

    if current_time.hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_time.hour < 18:
        greeting = "Good Afternoon!"
    elif 18 <= current_time.hour < 21:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"

    return render(request, 'greet.html', {'greeting': greeting})

