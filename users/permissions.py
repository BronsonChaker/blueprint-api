from .models import Membership

# Permission list for different user role types
RULES = {
    'create_vendor': ['owner', 'admin'],
    'create_job': ['owner', 'admin'],
    'delete_job': ['owner', 'admin'],
    'edit_job': ['owner', 'admin'],
    'create_task': ['owner', 'admin', 'supervisor'],
    'edit_task': ['owner', 'admin', 'supervisor'],
    'create_inspection': ['owner', 'admin', 'supervisor', 'inspector'],
    'submit_inspection': ['owner', 'admin', 'supervisor', 'inspector'],
    'manage_user': ['owner', 'admin']
}

def has_permission(user, organisation, action):
    """If user inside of an organisation has the permission to complete and action True will be retuned."""

    try:
        membership = Membership.objects.get(user=user, organisation=organisation)
    except Membership.DoesNotExist:
        return False

    allowed_roles = RULES.get(action, [])

    return membership.role in allowed_roles

   