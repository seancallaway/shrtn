from django.shortcuts import get_object_or_404, reverse
from django.views.generic import CreateView, DetailView, RedirectView

from redirect.models import Redirect


class DoRedirect(RedirectView):
    permanent = False
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        redirect = get_object_or_404(Redirect, slug=kwargs['slug'])
        return redirect.target


class HomePageView(CreateView):
    template_name = 'index.html'
    model = Redirect
    fields = ['target']

    def get_success_url(self):
        return reverse('show-link', kwargs={'slug': self.object.slug})


class LinkSuccessView(DetailView):
    template_name = 'show_link.html'
    model = Redirect
    context_object_name = 'my_link'
