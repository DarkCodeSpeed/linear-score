from django import forms

class StudentForm(forms.Form):
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    race_ethnicity = forms.CharField(max_length=100)
    parental_education = forms.CharField(max_length=100)
    lunch = forms.ChoiceField(choices=[('standard', 'Standard'), ('free/reduced', 'Free/Reduced')])
    test_preparation = forms.ChoiceField(choices=[('none', 'None'), ('completed', 'Completed')])
    math_score = forms.FloatField(required=True)  # Add this field
    reading_score = forms.FloatField(required=True)  # Add this field
