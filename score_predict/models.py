from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    time_of_study = models.FloatField()  # Hours of study
    attendance_percentage = models.FloatField()  # Attendance percentage
    breaks_taken = models.IntegerField()  # Number of breaks during study
    score = models.FloatField(null=True, blank=True)  # Actual Score (optional, for already scored students)

    def __str__(self):
        return self.name
