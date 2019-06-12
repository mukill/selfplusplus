from django import forms
from pagedown.widgets import PagedownWidget
from .models import BlogPost 
from crispy_forms.layout import Layout, MultiWidgetField
from crispy_forms.helper import FormHelper

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'image',
            'slug',
            'content',
            'publish_date'
        ]
        labels = {
        }
        widgets = {
            'publish_date': forms.SelectDateWidget(),
            'content': PagedownWidget()
        }
    
    def __init__(self, *args, **kwargs):
        super(BlogPostModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'form-horizontal'
        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
            'title',
            'image',
            'slug',
            'content',
            MultiWidgetField(
                'publish_date',
                attrs=(
                    {'style': 'width: 32.8%; display: inline-block;'}
                )
            ),
        )

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title