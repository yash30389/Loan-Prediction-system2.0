![](Django-app/customerLoanUI.PNG?raw=true)
# Loan prediction system
Project aims to predict if a customer will get a loan given applicant income, loan amount, credit history, education status, self-employment status, property area, etc. A model is trained using the training data on previous customers' loan approval history. Later, additional customer information can be leveraged to train a bigger model.

• The web service is developed using the Django framework & REST API. <br>
• To build the model, Tensorflow 2.0 is used. <br>
• SMOTE is used to oversample the minority class (i.e., loan rejection).<br>
• The data is normalized and preprocessed. <br>
• The model has an accuracy of 80%. <br>

# Performance:
<img src="accuracy.PNG" width="70%">
<img src="loss.PNG" width="70%">
<img src="confusionMatrix.PNG" width="70%">

# How to run:
To check the model please open the following file:<br>
> Customer_Loan.ipynb <br>
<br>
To run the web service, go inside the Django-app directory and run the following commands:<br>
> pip install requirements.txt <br>
> python manage.py makemigrations <br>
> python manage.py migrate<br>
> python manage.py runserver<br>
<br>

=========================================================
# password for test name=samir password=samir@1234

=========================================================
super admin password
---------------------------------------------------------
yash30389@gmail.com
yash@1234
---------------------------------------------------------