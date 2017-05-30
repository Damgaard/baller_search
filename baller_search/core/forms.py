from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class PostForm(SearchForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Fieldset(
                '',
                'q',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white btn-lg')
            )
        )
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['q'].widget.attrs.update(
            {'autofocus': 'autofocus',
             'placeholder': 'AMA'}
        )

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(PostForm, self).search()

        if self.cleaned_data['q'].lower() in ["", "all"]:
            return SearchQuerySet().all().order_by('-score_i')

        if not self.is_valid():
            return self.no_query_found()

        return sqs
