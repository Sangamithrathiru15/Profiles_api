#to provide the permissions class
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
#:to create custom permission classes
    """allow users to edit their own profile"""

    def has_object_permission(self,request,view,obj):#this method will be called when everytime when the api is called
        """check the user is trying to edit their own profile"""
        #HTTP method-get,put,patch,DELETE
        #safe method-http get
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id#for update/delete where user profile will be atttached wi    th the rquest parameterso that it can be compared with object
