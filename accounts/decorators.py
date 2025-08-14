from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

def role_required(role: str):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('accounts:login')
            if request.user.user_type != role:
                return HttpResponseForbidden('You do not have access to this page.')
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
