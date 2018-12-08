from django.shortcuts import redirect
from django.contrib import messages

def HotelUser(function):
    def wrapping_func(request,*args,**kwrds):
        if request.user.is_authenticated:
            if request.user.user_profile.rest:
                return function(request,*args,**kwrds)

            else:
                messages.error(request,f'You are not a Hotel manager')
                return redirect('Users-Home')

        else:
            messages.error(request,f'You are not logged in.')
            return redirect('Rest-Login')

    return wrapping_func
