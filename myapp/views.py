from django.shortcuts import get_object_or_404, redirect, render
from django.views import *

from .form import *

from .models import *

# Create your views here.

class Feedback(View):
    def get(self, request):
        c = Feedback_model.objects.all()
        return render(request, 'viewFeedback.html', {'s':c})
    
class Reply(View):
    def get(self, request, pk):
        fb = get_object_or_404(Feedback_model, pk = pk)
        print(fb)
        return render(request, 'reply.html', {'feed':fb})
    
    def post(sekf, request, pk):
        fb = get_object_or_404(Feedback_model, pk = pk)
        form = Reply_form(request.POST, instance=fb)
        if form.is_valid():
            form.save()
            return redirect('viewfeedback')
        

class View_complaint(View):
    def get(self, request):
        c = Complaint_model.objects.all()
        return render(request, 'complaint.html', {'s':c})


