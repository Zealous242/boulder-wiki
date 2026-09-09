from django.conf import settings
from django.db import models

from articles.models import Article


class SuggestedEdit(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='suggested_edits')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='suggested_edits')
    proposed_content = models.TextField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.article.title} - {self.user.username} ({self.status})'
