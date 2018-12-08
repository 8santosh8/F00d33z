from django.shortcuts import redirect

def Details_Required(function):
    def wrapping_func(request,*args,**kwrds):
        if request.user.is_authenticated:
            if not hasattr(request.user, 'user_profile'):
                return redirect('Users-AddDetails')
            else:
                return function(request,*args,**kwrds)
        else:
            return redirect('Users-Login')
    return wrapping_func
