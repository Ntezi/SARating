from django.db.models import Avg

from django.views.generic import TemplateView, DetailView, ListView
from .models import Business


# Create your views here.

class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'ratings/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context


class BusinessListView(ListView):
    model = Business
    context_object_name = 'businesses'
    ordering = ['-ratings']
    paginate_by = 20  # if pagination is desired
    template_name = 'ratings/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_average = Business.objects.aggregate(Avg('total_reviews'))
        c_average = c_average["total_reviews__avg"]
        context['c_average'] = c_average
        return context


class BusinessDetailView(DetailView):
    pass
