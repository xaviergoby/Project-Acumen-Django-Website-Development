from django.shortcuts import render
from django.shortcuts import redirect
# from users.forms import CustomUserCreationForm
from users.forms import PorfileInfoForm
from users.forms import CustomUserCreationForm
from django.contrib import messages
from django.views.generic.base import TemplateView
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

class HomePageCBV(TemplateView):
    template_name = 'users/home_page.html'
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return render(request, self.template_name, {"form": form})
        return render(request, self.template_name, {"form": form})


class ProfileInfoCBV(TemplateView):
    # template_name = 'users/profile_info.html'
    template_name = 'users/profile.html'
    form_class = PorfileInfoForm

    def get(self, request, *args, **kwargs):
        # form = request.
        form = self.form_class()
        return render(request, self.template_name, {"form":form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # first_favourite_subject = form.cleaned_data['first_favourite_subject']
            # second_favourite_subject = form.cleaned_data['second_favourite_subject']
            # print(form.clean())
            return render(request, self.template_name, {"form": form})

        return render(request, self.template_name, {"form": form})


def join(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # new_user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for {0}".format(username))
            return redirect('login') # og: 'login'
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/join.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated is False:
        username = request.user.username
        password = request.user.password
        # username = request.POST['username']
        # password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('grind')
    else:
        return redirect('test_view')