from datetime import date

from haystack.generic_views import SearchView
from .forms import PostForm
from .models import Post


class MySearchView(SearchView):
    """My custom search view."""
    template_name = "pages/home.html"
    form_class = PostForm

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        # further filter queryset based on some set of criteria
        return queryset.order_by('-score_i')

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        return context
