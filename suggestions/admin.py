from django.contrib import admin

from articles.models import Article
from .models import SuggestedEdit


@admin.register(SuggestedEdit)
class SuggestedEditAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('article__title', 'user__username')
    ordering = ('-created_at',)
    actions = ['approve_suggestions', 'reject_suggestions']

    @admin.action(description='Approve selected pending suggestions')
    def approve_suggestions(self, request, queryset):
        pending = queryset.filter(status='pending')
        for suggestion in pending:
            article = suggestion.article
            article.content = suggestion.proposed_content
            article.save(update_fields=['content'])
            suggestion.status = 'approved'
            suggestion.save(update_fields=['status'])

    @admin.action(description='Reject selected suggestions')
    def reject_suggestions(self, request, queryset):
        pending = queryset.filter(status='pending')
        for suggestion in pending:
            suggestion.status = 'rejected'
            suggestion.save(update_fields=['status'])
