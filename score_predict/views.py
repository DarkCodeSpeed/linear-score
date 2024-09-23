import os
import joblib
import numpy as np
import pandas as pd  # Import pandas for DataFrame handling
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.conf import settings

from django.utils import translation
from django.contrib import messages

pipeline = None  # Global variable for the loaded pipeline

def load_model():
    global pipeline
    if pipeline is None:
        model_path = os.path.join(settings.BASE_DIR, 'student_score_model.pkl')
        pipeline = joblib.load(model_path)


def predict_score(request):
    load_model()  # Load the model when the page loads
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            race_ethnicity = form.cleaned_data['race_ethnicity']
            parental_education = form.cleaned_data['parental_education']
            lunch = form.cleaned_data['lunch']
            test_preparation = form.cleaned_data['test_preparation']
            math_score = form.cleaned_data['math_score']
            reading_score = form.cleaned_data['reading_score']

            # Validate score ranges
            if math_score < 0 or math_score > 100:
                messages.error(request, 'Math score must be between 0 and 100.')
                return render(request, 'predict_score.html', {'form': form})

            if reading_score < 0 or reading_score > 100:
                messages.error(request, 'Reading score must be between 0 and 100.')
                return render(request, 'predict_score.html', {'form': form})

            # Prepare input for prediction as a DataFrame
            test_input = pd.DataFrame([[gender, race_ethnicity, parental_education, lunch, test_preparation, math_score, reading_score]],
                                       columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score'])

            # Predict scores
            predicted_scores = pipeline.predict(test_input)

            return render(request, 'predict_score.html', {'form': form, 'predicted_scores': predicted_scores})
    else:
        form = StudentForm()

    return render(request, 'predict_score.html', {'form': form})






def home(request):
    user_language = request.LANGUAGE_CODE
    return render(request, 'home.html', {'user_language': user_language})

def set_language(request):
    if 'language' in request.POST:
        language = request.POST['language']
        translation.activate(language)
        request.session[translation.LANGUAGE_SESSION_KEY] = language
    return redirect('home')
