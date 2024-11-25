from functools import wraps
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user or not request.user.is_authenticated:
                return Response({"error": "Authentication required"}, status=HTTP_403_FORBIDDEN)
            if hasattr(request.user, 'role') and request.user.role not in roles:
                return Response({"error": "Access denied"}, status=HTTP_403_FORBIDDEN)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator