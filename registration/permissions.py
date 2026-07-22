from django.http import HttpResponse
# from functools import wraps

# def permit(allowed_roles):
#     def decorator(view_func):
#         @wraps(view_func)
#         def wrapper(request, *args, **kwargs):
#             if not request.user.is_authenticated or request.user.role not in allowed_roles:
#                 return HttpResponse("Access denied!")
#             return view_func(request, *args, **kwargs)
#         return wrapper
#     return decorator

def permit(allowed_roles):
    def check_availability(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role not in allowed_roles:
            return HttpResponse(f"Access denied for the role of {request.user.role}!")
        return allowed_roles(request, *args, **kwargs)
    return check_availability

# 1 CEO
# 2 Branch Director
# 3 Academic Manager
# 4 HR Manager
# 5 Receptionist
# 6 Teacher
# 7 Accountant
# 8 Student
# 9 Parent
