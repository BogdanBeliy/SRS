from django.shortcuts import render
from django.views.generic import TemplateView

class BaseView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'user_id': '199ffc36-283b-42f4-b2b6-c727b441cc55'})

