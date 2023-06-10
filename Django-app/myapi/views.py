from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from .models import approvals
from .serializers import approvalSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from .forms import approvalForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm


class approvalView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalSerializers


def ohevalue(df):
    ohe_col = joblib.load('myapi/allcol.pkl')
    cat_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict = {}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)
    return newdf


def setGpu():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            # Restrict TensorFlow to only use the fourth GPU
            tf.config.experimental.set_visible_devices(gpus[0], 'GPU')

            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            logical_gpus = tf.config.experimental.list_logical_devices('GPU')
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            print(e)


def approveReject(unit):
    try:
        setGpu()
        model = tf.keras.models.load_model('myapi/customer_loan.h5')
        scalers = joblib.load("myapi/scaler.pkl")
        unit['LoanAmount'] = int(unit['LoanAmount']) / 1000
        # print(unit)
        X = scalers.transform(unit)
        y_pred = model.predict(X)
        y_pred = (y_pred > 0.58)
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        newdf = newdf.replace({True: 'Approved', False: 'Rejected'})
        return ('Your status is {}'.format(newdf))
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def cxcontact(request):
    postFlag = 0
    if request.method == 'POST':
        # approvalForm is defined in forms.py
        form = approvalForm(request.POST)
        if form.is_valid():
            Firstname = form.cleaned_data['firstname']
            Lastname = form.cleaned_data['lastname']
            Dependants = form.cleaned_data['Dependants']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
            LoanAmount = form.cleaned_data['LoanAmount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            answer = approveReject(ohevalue(df))
            check = answer.split()[-1]

            object = approvals()
            object.first_name = Firstname
            object.last_name = Lastname
            object.dependants = Dependants
            object.applicant_income = ApplicantIncome
            object.coapplicant_income = CoapplicantIncome
            object.loan_amount = LoanAmount
            object.loan_term = Loan_Amount_Term
            object.credit_history = Credit_History
            object.gender = Gender
            object.married = Married
            object.graduate_education = Education
            object.self_employed = Self_Employed
            object.area = Property_Area
            object.save()

            if check == "Rejected":
                postFlag = 2
            else:
                postFlag = 1
            messages.success(request, 'Application Status: {}'.format(answer))

    form = approvalForm()
    return render(request, 'myform/cxform.html', {'form': form, 'postFlag': postFlag})


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request,'login.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             # handle the signup process (e.g. create a user and log them in)
#             return redirect('home')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def lognout(request):
    return render(request, 'index.html')