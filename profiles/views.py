from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profiles.decorators import is_profile_owner
from profiles.forms import ProfileCreationForm
from profiles.models import Profile

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('practice:exercise')
    template_name = 'profiles/new.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(is_profile_owner,'get')
@method_decorator(is_profile_owner,'post')

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    success_url = reverse_lazy('practice:exercise')
    template_name = 'profiles/modify.html'