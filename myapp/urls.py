from django.urls import path

from .views import *

urlpatterns = [
    path('viewfeedback/', Feedback.as_view(), name='viewfeedback'),
    path('reply/<int:pk>', Reply.as_view(), name='reply'),
    path('viewComplaint', View_complaint.as_view(), name='viewComplaint'),
]
