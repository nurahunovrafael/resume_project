from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ResumeForm

class ResumeFormView(FormView):
    form_class = ResumeForm
    template_name = 'cv/resume_form.html'
    success_url = '/resume/resume/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.cleaned_data
        form.save()
        return super().form_valid(form)

