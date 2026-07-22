from django import forms
from .models import Assessment, AssessmentRequest, AssessmentResponse

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['lesson', 'title', 'description']

class AssessmentRequestForm(forms.ModelForm):
    class Meta:
        model = AssessmentRequest
        fields = ['assessment', 'text', 'max_score', 'order']

class AssessmentResponseForm(forms.ModelForm):
    class Meta:
        model = AssessmentResponse
        fields = ['question', 'student', 'answer_text', 'score', 'feedback', 'checked_by']