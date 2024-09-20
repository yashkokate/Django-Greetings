from django.http import HttpResponse
from django.shortcuts import render

# View to set a cookie
def set_cookie(request):
    response = HttpResponse("Cookie has been set.")
    response.set_cookie('username', 'DjangoUser', max_age=3600)  # cookie expires in 1 hour
    return response

# View to retrieve and display the cookie
def get_cookie(request):
    username = request.COOKIES.get('username', 'No cookie found')
    return HttpResponse(f'Cookie value: {username}')

# View to set a session
def set_session(request):
    request.session['username'] = 'DjangoUserSession'
    return HttpResponse("Session has been set.")

# View to retrieve and display the session
def get_session(request):
    username = request.session.get('username', 'No session found')
    return HttpResponse(f'Session value: {username}')

# Combined view to display both cookie and session data in a template
def show_info(request):
    cookie_username = request.COOKIES.get('username', 'No cookie set')
    session_username = request.session.get('username', 'No session set')
    
    context = {
        'cookie_username': cookie_username,
        'session_username': session_username,
    }
    
    return render(request, 'info.html', context)
def set_cookie_and_session(request):
    # Set a cookie
    response = HttpResponse("Cookie and Session have been set.")
    response.set_cookie('username', 'DjangoCookieUser', max_age=3600)  # Cookie expires in 1 hour
    
    # Set a session
    request.session['username'] = 'DjangoSessionUser'
    
    return response


