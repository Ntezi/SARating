from django.db.models import Avg

from django.views.generic import TemplateView, DetailView, ListView
from .models import Business


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer



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
    # paginate_by = 50  # if pagination is desired
    template_name = 'ratings/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_average = Business.objects.aggregate(Avg('total_reviews'))
        c_average = c_average["total_reviews__avg"]
        context['c_average'] = c_average
        return context


class BusinessDetailView(DetailView):
    pass


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer