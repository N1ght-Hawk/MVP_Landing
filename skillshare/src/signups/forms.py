from django import forms


from .models import signup

class signupform(forms.ModelForm):
    class Meta:
       # print "Came here"
        model = signup
    #    fields = ['first_name', 'last_name', 'email']

