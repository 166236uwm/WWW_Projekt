from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def role_required(required_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

            user_role = getattr(request.user, 'role', None)
            if user_role not in required_roles:
                return Response({"error": f"User does not have the required role: {required_roles}"}, status=status.HTTP_403_FORBIDDEN)

            return view_func(request, *args, **kwargs)
        return wrapped_view
    return decorator
