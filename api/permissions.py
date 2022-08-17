from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsRestaurantAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        try:
            return request.method in SAFE_METHODS or request.user.role == 'Restaurant'
        except:
            return request.user.is_authenticated


class RestaurantOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return request.method in SAFE_METHODS or obj.user == request.user
        except:
            return request.user.is_authenticated


class RestaurantOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Restaurant'


class MenuAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return request.method in SAFE_METHODS or obj.restaurant.user == request.user
        except:
            return request.user.is_authenticated


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'Employee'


class IsCurrentEmployee(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.user == request.user and request.user.role == 'Employee'
