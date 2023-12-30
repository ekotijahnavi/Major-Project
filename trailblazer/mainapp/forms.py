from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django import forms


import re;


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email' : 'Email'}
    def clean_username(self):
        uname=self.cleaned_data['username']
        if uname.isdigit()==True:
            raise forms.ValidationError("You should enter only combinations of alphanumericals or only alphabets")
        elif len(uname)<4:
            raise forms.ValidationError("username should be atleat 4 characters")
        return uname
    def clean_first_name(self):
        fname=self.cleaned_data['first_name']
        match=re.fullmatch('[A-Za-z]+\s{,1}[A-Za-z]*',fname)
        if match == None:
            raise forms.ValidationError("Enter valid name")
        elif len(fname)<3:
            raise forms.ValidationError("first name should contain atleast 3 characters")
        return fname
    def clean_last_name(self):
        lname=self.cleaned_data['last_name']
        match=re.fullmatch('[A-Za-z]+\s{,1}[A-Za-z]*',lname)
        if match == None:
            raise forms.ValidationError("Enter valid name")
        return lname
    def clean_email(self):
        mail=self.cleaned_data['email']
        
        match1=re.fullmatch('^[a-z][a-z0-9._%+-]*@gmail.com',mail)
        if len(mail)==0:
            raise forms.ValidationError("This Field is Required")
        elif match1 == None:
            raise forms.ValidationError('gmail must start with alphabet')
        return mail
    def clean_password1(self):
        passwd = self.cleaned_data['password1']
        upper=0
        lower=0
        digit=0
        other=0
        if len(passwd)<8:
            raise forms.ValidationError('Password must be 8 Character or more')
        for i in range(len(passwd)):
            if(passwd[i].isupper() == True):
                upper=upper+1
            elif(passwd[i].islower()== True):
                lower=lower+1
            elif(passwd[i].isdigit() == True):
                digit=digit+1
            else:
                other=other+1
            
        if digit<1:
            raise forms.ValidationError('Password must include a digit')
        elif upper<1:
            raise forms.ValidationError('Password must include a upper case letter')
        elif lower<1:
            raise forms.ValidationError('Password must include a lower case letter')
        elif other<1:
            raise forms.ValidationError('Password must include a special character')

        return passwd

