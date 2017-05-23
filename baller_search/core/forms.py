from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class PostForm(SearchForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
            'Make a query! Find baller posts!',
            'q',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
        super(PostForm, self).__init__(*args, **kwargs)

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(PostForm, self).search()

        if self.cleaned_data['q'].lower() == "all":
            return SearchQuerySet().all().order_by('-score_f')

        if not self.is_valid():
            return self.no_query_found()

        return sqs
