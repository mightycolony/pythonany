from django.shortcuts import render
from user_app_auth import forms
#UserForm, UserProfileInfoForm
# Create your views here.

#for login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#if we ever wanted a view to required the user to be logged in, we can decorate it with this login_required



def index(request):
    return render(request,'user_app_auth/index.html')

@login_required
def special(reqeust):
    return HttpResponse("YOU are logge in NICE!")
 
#The way without this decorator,the actually require a user to be logged in to be logged out
#@login_required -> in order to make sure that any view requires a person login to see it
#we need to use this login_required
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request): 
    
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #Grabbing the user form and saving it to the database
            user = user_form.save()
            #hashing the password by  set password method (we set in settings.py)
            user.set_password(user.password)
            #then we save the password to database
            user.save()

            #since we haven't saved it to db, otherwise we may get erros with collision where it tried to
            # to overwrite the user -> (user = user_form.save())
            profile = profile_form.save(commit=False)
            #for that we going add the below line.
            
            # This sets up that 1  to 1 relationship
            #user = models.OneToOneField(User,on_delete=models.DO_NOTHING) -> models.py
            #the userprofileinfo model is having one to one relationship with the user.
            # so this 1 to 1 relationship, is defined in the views with the below line of code,
            profile.user = user

            #so basically we relating that extra profile infomration to the user modelform



            # so we are going to say request.FILES to actually find those and we will be dealoing with
            #key based on what we defined in the models
            if 'profile_picture' in request.FILES: #request.FILES coz image is a file
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()

            registered = True
        else:
            print(user_form.errros,profile_form.errors)
    else:
        print(registered)
        user_form = forms.UserForm()
        profile_form= forms.UserProfileInfoForm()
        print('form created')

    return render(request,'user_app_auth/registration_page.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered': registered
                   })


#sometimes django reports error when using login as function name
#from django.contrib.auth import authenticate,login,logout  - > coz we import login
def user_login(request):
    if request.method ==  "POST":
                # <input type="text" name="username" placeholder="Enter username">
                #  in the input we gave name as username so we getting that here
        username = request.POST.get('username')
        password = request.POST.get('password')

        #this will authenticate the user for us
        user = authenticate(username=username,password=password)

        if user:
            #checking the account is active    
            if user.is_active:
                #login the user
                login(request,user) # the user is a object that is returned by authenticate
                # so if the user login and sucessfull and active and reverse them and redirect 
                # them index page
                
                return HttpResponseRedirect(reverse('index'))
            else:
               return HttpResponse("Account not active") 
        else:
            print("someone trying to login and failed")
            print("username:{} and password{}".format(username,password))
        return HttpResponse("invalid login details supplied")
    
    else:
        return render(request,'user_app_auth/login.html',{})