from .models import UserDetails
from django.contrib.auth.models import User

def check_seller(request):

    # print(request.user)
    
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user.username)
        userDetails = UserDetails.objects.get(user = user)

        if userDetails.is_seller:

            userBool =  True

        else: 
            
            userBool =  False
    else: 
        userBool = False

    return {'is_seller': userBool}