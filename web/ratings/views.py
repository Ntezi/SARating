from django.db.models import Avg

from django.views.generic import TemplateView, DetailView, ListView
from .models import Business

from django.shortcuts import get_object_or_404, render


# Create your views here.

def business_detail_view(request, id):
    business = Business.objects.get(id=id)
    print(business)

    # business = get_object_or_404(Business, pk)
    context = {'business': business}
    return render(request, 'ratings/detail.html', context)


def about(request):
    return render(request, 'ratings/about.html')


def report(request):
    return render(request, 'ratings/report.html')


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
    # paginate_by = 50  # if pagination is desired
    template_name = 'ratings/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_average = Business.objects.aggregate(Avg('total_reviews'))
        c_average = c_average["total_reviews__avg"]
        context['c_average'] = c_average
        return context


class BusinessDetailView(DetailView):
    model = Business
    context_object_name = 'business'
    # slug_field = 'name'
    # slug_url_kwarg = 'name'
    template_name = 'ratings/detail.html'

    def get(self, request, id):
        business = Business.objects.get(_id=id)
        context = {'business': business}
        return render(request, 'ratings/detail.html', context)


class ReportView(TemplateView):
    model = Business
    context_object_name = 'businesses'
    # paginate_by = 50  # if pagination is desired
    template_name = 'ratings/report.html'


class PopularView(ListView):
    model = Business
    context_object_name = 'businesses'
    ordering = ['-total_reviews']
    # paginate_by = 50  # if pagination is desired
    template_name = 'ratings/popular.html'
