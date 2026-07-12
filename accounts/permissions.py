from django.http import HttpResponse

def permit_creating(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.role in ['admin', 'manager']:
                return HttpResponse('Access denied!')
        else:
            return HttpResponse('Access denied!')
        return func(request, *args, **kwargs)
    return wrapper

# CEO /
        # View all branches
        # Create, edit, and deactivate branches
        # View financial reports across all branches
        # View employee statistics
        # View student statistics
        # View academic performance reports
        # Approve major decisions
        # View HR reports
        # View attendance reports
        # View system analytics
        # View dashboards
        # Export reports
# Branch Director
# Academic Manager
# HR Manager
# Receptionist
# Teacher
# Accountant
# Student,
# Parent
# System Administrator