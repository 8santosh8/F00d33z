from django.shortcuts import redirect
from django.contrib import messages

def Details_Required(function):
    def wrapping_func(request,*args,**kwrds):
        if request.user.is_authenticated:
            if not hasattr(request.user, 'user_profile'):
                messages.error(request,f'First add few details to continue')
                return redirect('Users-AddDetails')
            else:
                return function(request,*args,**kwrds)
        else:
            messages.error(request,f'You need to login first')
            return redirect('Users-Login')
    return wrapping_func
