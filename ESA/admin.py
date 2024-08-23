from django.contrib import admin
from .models import Email, EmailAnalysis

class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    search_fields = ('content',)

# class EmailAnalysisAdmin(admin.ModelAdmin):
#     def email_content(self, obj):
#         # Display the first 50 characters of the related Email content
#         # return obj.email.content[:50]
    
#     # email_content.short_description = 'Email Content'  # Optional: Set a human-readable name for the column

#     list_display = ('email_content', 'sentiment')  # Display email content snippet and sentiment
#     search_fields = ('email__content', 'sentiment')

admin.site.register(Email, EmailAdmin)
# admin.site.register(EmailAnalysis, EmailAnalysisAdmin)



class EmailAnalysisAdmin(admin.ModelAdmin):
    # Display the fields you want in the admin list view
    list_display = ('content', 'sentiment_huggingface', 'sentiment_berttweet')
    # Allow searching by content and sentiment
    search_fields = ('content', 'sentiment_huggingface', 'sentiment_berttweet')

admin.site.register(EmailAnalysis, EmailAnalysisAdmin)