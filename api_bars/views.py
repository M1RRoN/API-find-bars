from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from api_bars.serializers import CreateUserSerializer
from establishments.models import Place


def index(request):
    return render(request, 'index.html')


class SearchView(ListView):
    model = Place
    template_name = 'search_results.html'
    context_object_name = 'places'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            results = Place.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            return results
        else:
            return Place.objects.none()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)

class CustomLoginView(LoginView):
    template_name = 'login.html' # здесь указываем имя шаблона для страницы входа

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me') # здесь можно получить значение поля remember_me из формы входа
        if not remember_me:
            self.request.session.set_expiry(0) # если remember_me не выбрано, то сессия будет действительна только до закрытия браузера
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
