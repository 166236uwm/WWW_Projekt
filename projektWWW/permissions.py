from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    """
    Uprawnienia bazujące na rolach użytkownika.
    """
    allowed_roles = ['admin', 'manager', 'POS']  # Role, które mają dostęp

    def has_permission(self, request, view):
        # Sprawdza, czy użytkownik jest uwierzytelniony
        if not request.user or not request.user.is_authenticated:
            return False

        # Sprawdza, czy użytkownik ma odpowiednią rolę
        if hasattr(request.user, 'role') and request.user.role in self.allowed_roles:
            return True

        return False