from django import forms
from .models import approvals

class approvalModelForm(forms.ModelForm):
    class Meta:
        model = approvals
        fields = "__all__"

class approvalForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
    lastname = forms.CharField(label='Last Name', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
    Dependants = forms.IntegerField(label='Dependants', widget=forms.NumberInput(attrs={'placeholder': 'Enter number of dependants'}))
    ApplicantIncome = forms.IntegerField(label='Applicant Income', widget=forms.NumberInput(attrs={'placeholder': 'Enter monthly gross income'}))
    CoapplicantIncome = forms.IntegerField(label='Co-Applicant Income', widget=forms.NumberInput(attrs={'placeholder': 'Enter co-applicant monthly gross income'}))
    LoanAmount = forms.IntegerField(label='Loan Amount', widget=forms.NumberInput(attrs={'placeholder': 'Requested loan amount'}))
    Loan_Amount_Term = forms.IntegerField(label='Loan Amount Term', widget=forms.NumberInput(attrs={'placeholder': 'Loan term in months'}))
    Credit_History = forms.ChoiceField(label='Credit Score', choices=[('0','580-669'), ('1','670-739'), ('2', '740-799'), (3, '800-850')])
    Gender = forms.ChoiceField(label='Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    Married = forms.ChoiceField(label='Marital Status', choices=[('Yes', 'Yes'), ('No', 'No')])
    Education = forms.ChoiceField(label='Education Status', choices=[('Graduate', 'Graduated'), ('Not_Graduate', 'Not Graduated')])
    Self_Employed = forms.ChoiceField(label='Self Employed', choices=[('Yes', 'Yes'), ('No', 'No')])
    Property_Area = forms.ChoiceField(label='Property Area', choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')])

# class SignupForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=100)
#     email = forms.EmailField(label='Email')
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_confirm = cleaned_data.get("password_confirm")

#         if password != password_confirm:
#             raise forms.ValidationError("Passwords do not match")