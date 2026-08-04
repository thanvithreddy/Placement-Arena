from django.urls import path
from .views import IngestTextbookView, TrueAIRAGAskView, RecordTelemetryView

urlpatterns = [
    path('ingest/', IngestTextbookView.as_view(), name='textbook-ingest'),
    path('rag-ask/', TrueAIRAGAskView.as_view(), name='textbook-rag-ask'),
    path('telemetry/', RecordTelemetryView.as_view(), name='textbook-telemetry'),

    path('upload-pdf/', PDFDocumentUploadView.as_view(), name='textbook-upload-pdf'),
    path('chat/', AITutorChatView.as_view(), name='textbook-chat'),

    path('documents/', DocumentListDeleteView.as_view(), name='textbook-documents-list'),
    path('documents/<int:pk>/', DocumentListDeleteView.as_view(), name='textbook-documents-delete'),


]
