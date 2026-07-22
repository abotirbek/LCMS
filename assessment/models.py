from django.db import models
from accounts.models import Student, TimeStamped
from education.models import Lesson

# Create your models here.
class Assessment(TimeStamped):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='assessments')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class AssessmentRequest(TimeStamped):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='requests')
    text = models.TextField()
    max_score = models.PositiveSmallIntegerField(default=10)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(fields=['assessment', 'order'], name='unique_question_order'),
        ]

    def __str__(self):
        return f'{self.normativ} — question {self.order}'


class AssessmentResponse(TimeStamped):
    question = models.ForeignKey(AssessmentRequest, on_delete=models.CASCADE, related_name='responses')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assessment_responses')
    answer_text = models.TextField()
    score = models.PositiveSmallIntegerField(null=True, blank=True)
    feedback = models.TextField(blank=True)
    checked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checked_answers',
    )
    checked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'student'], name='unique_answer'),
        ]

    def __str__(self):
        return f'{self.student} — {self.question}'

    @property
    def is_checked(self):
        return self.score is not None