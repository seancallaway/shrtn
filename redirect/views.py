from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from redirect.models import Redirect


class DoRedirect(RedirectView):
    permanent = False
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        redirect = get_object_or_404(Redirect, slug=kwargs['slug'])
        return redirect.target
