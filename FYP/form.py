from django import forms

class Donate(forms.Form):
    purpose_of_donation=[
        ('Education','Education'),
        ('Health','Health'),
        ('Start_Up','Start Up'),
        ('political_Party','political Party'),
        ('Disaster_Relief','Disaster Relief'),
        ('Social_Services ','Social Services '),
        ('Human_Right ','Human Right')

    ]
    Gender=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]

    First_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=10)
    email_Address=forms.EmailField()
    phone_Number=forms.DecimalField(min_value=0)
    Purpose=forms.ChoiceField(choices=purpose_of_donation)
    
class Data_Getting(forms.Form):
    Name=forms.CharField(max_length=40)
    Father_Name=forms.CharField(max_length=40)
    Mother_Name=forms.CharField(max_length=40)