from django.contrib import admin
from .models import Document, DocumentChunk, StudentBKTTracker, TelemetryLog

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject', 'topic_slug', 'file_name', 'uploaded_by', 'created_at', 'get_chunk_count')
    list_filter = ('subject', 'created_at')
    search_fields = ('title', 'file_name', 'subject', 'topic_slug')
    actions = ['delete_selected_documents']

    def get_chunk_count(self, obj):
        return obj.chunks.count()
    get_chunk_count.short_description = 'Vector Chunks'

    @admin.action(description='Delete selected documents and all vector chunks')
    def delete_selected_documents(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"Successfully deleted {count} document(s) and all associated vector RAG chunks!")

@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):
    list_display = ('id', 'document', 'subject', 'topic_slug', 'chapter_title', 'chunk_index', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('content', 'chapter_title', 'subject', 'topic_slug')

@admin.register(StudentBKTTracker)
class StudentBKTTrackerAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'topic_slug', 'mastery_probability', 'review_count', 'last_reviewed_at')
    list_filter = ('subject',)

@admin.register(TelemetryLog)
class TelemetryLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'cognitive_state', 'wpm', 'backspace_count', 'pause_duration_ms', 'created_at')
    list_filter = ('cognitive_state', 'subject')
