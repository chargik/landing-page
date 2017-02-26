from django.shortcuts import render
from django.views.generic import View, FormView, CreateView
from newsletter.forms import JoinForm
# Create your views here.

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "pages/home.html", {})


class HomeView(CreateView):
    template_name = 'pages/home.html'
    form_class = JoinForm
    success_url = '/'

    #def form_valid(self, form):